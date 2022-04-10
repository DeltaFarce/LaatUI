import os
import re

import oss2

from LaatUI.LaatUI.settings import BASE_DIR
from pathlib import Path


def upload():
    # 上传到OSS
    auth = oss2.Auth('LTAI5tF4791LWMiwpv3JpwwM', 'QKHek3tfxknwjYpWLuzYWVBDyGTPsQ')
    endpoint = 'https://oss-cn-beijing.aliyuncs.com'
    bucket = oss2.Bucket(auth, endpoint, 'laatui')
    # with open('/Users/sunxinyang/Desktop/LaatUI/LaatUI/Cy/cypress/integration/img_2.png', 'rb') as f:
    with open('/Users/sunxinyang/Desktop/LaatUI.zip', 'rb') as f:
        bucket.put_object('Base/laatui-end-4-4.zip', f.read())
    # bucket.put_object('screenshots/88.png', '/Users/sunxinyang/Desktop/LaatUI/Cy/cypress/88.png')

    # print(os.path.abspath(f'/Users/sunxinyang/Desktop/LaatUI/LaatUI/Cy/cypress/integration/{path}'))
    # print(re.findall(r'[a-zA-Z0-9\:\/\\\_\-]*', '/Users/sunxinyang/Desktop/LaatUI/LaatUI/Cy/cypress/integration/')[0])
    # print(os.path.join('/Users/sunxinyang/Desktop/LaatUI/LaatUI/Cy/cypress/integration/', os.listdir('/Users/sunxinyang/Desktop/LaatUI/LaatUI/Cy/cypress/integration/')[0]))
    # print(os.path.join(f'{os.getcwd()}/Cy/cypress/screenshots/', os.listdir(f'{os.getcwd()}/Cy/cypress/screenshots/')[0]))
    # screenshots_path = os.path.join(f'{BASE_DIR}/Cy/cypress/screenshots/',
    #                                 os.listdir(f'{BASE_DIR}/Cy/cypress/screenshots/')[0])


upload()