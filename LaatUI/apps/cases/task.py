import time
from celery import shared_task
import os
import oss2
from datetime import datetime

from pathlib import Path
from reports.models import ReportModel


@shared_task
def celery_test():
    time.sleep(3)
    print("这是celery定时器测试！！！")

@shared_task
def celery_run_case(testcase, serializer):
    report_state = "成功"
    filename = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f')
    casepath = os.path.join(f'{os.getcwd()}/Cy/cypress/integration', filename + '.js')
    print(os.getcwd())
    with open(casepath, 'w') as f:
        f.write(testcase)

    # 运行脚本
    os.system(f'bash {os.getcwd()}/apps/cases/run_case.sh')
    with open(f'{os.getcwd()}/apps/cases/logs', 'r') as f:
        logs = f.read()

    # 删除运行完的脚本
    os.system(f'rm -fr {casepath}')

    # 上传到OSS
    auth = oss2.Auth('LTAI5tF4791LWMiwpv3JpwwM', 'QKHek3tfxknwjYpWLuzYWVBDyGTPsQ')
    endpoint = 'https://oss-cn-beijing.aliyuncs.com'
    bucket = oss2.Bucket(auth, endpoint, 'laatui')

    # 上传视频
    if os.path.exists(f'{os.getcwd()}/Cy/cypress/videos/'+filename+'.js.mp4'):
        print("开始上传视频")
        with open(f'{os.getcwd()}/Cy/cypress/videos/'+filename+'.js.mp4', 'rb') as f:
            bucket.put_object('videos/' + filename + '.mp4', f.read())

    # 上传失败截图
    if os.path.exists(f'{os.getcwd()}/Cy/cypress/screenshots/' + filename + '.js'):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        print(BASE_DIR)
        report_state = "失败"
        screenshots_path = os.path.join(f'{BASE_DIR}/Cy/cypress/screenshots/'+ filename + '.js',os.listdir(f'{BASE_DIR}/Cy/cypress/screenshots/{filename}.js')[0])
        print(screenshots_path)
        print(os.getcwd())
        with open(screenshots_path, 'rb') as f:
            bucket.put_object('screenshots/' + filename + '.png', f.read())

    # 创建报告
    ReportModel.objects.create(
        name=serializer.data['name'] + filename,
        log=logs,
        screenshot='https://laatui.oss-cn-beijing.aliyuncs.com/screenshots/' + filename + '.png' if os.path.exists(
            f'{os.getcwd()}/Cy/cypress/screenshots/' + filename + '.js') else '',
        video='https://laatui.oss-cn-beijing.aliyuncs.com/videos/' + filename + '.mp4',
        case_id=serializer.data['id'],
        project_id=serializer.data['project'],
        state=report_state
    )
    print("报告创建完成")