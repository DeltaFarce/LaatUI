# LaatUI
![image](https://user-images.githubusercontent.com/45864019/164970925-948e6748-fc76-4087-b9a9-fa28f2e0ec42.png)
##### 演示视频
https://laatui.oss-cn-beijing.aliyuncs.com/demo.mp4

已部署站点：http://121.196.214.215/donate （服务器性能较低，MySQL、redis、celery都部署在了一起，所以性能很差。。。。。。。）

LaatUI后端是使用Python编写的一个UI自动化工具，底层使用Cypress框架，借助了阿里的开源录制工具，录制对应的UI脚本，省去了页面定位编辑等复杂的步骤。
这里的应用只是初步的实现，实现了大盘、测试用例编辑、测试报告展示（报告包含失败的截图、运行的日志、运行的视频）、项目管理和项目运行设置。后期计划会添加PO思想、数据驱动等实现更高效用例编辑和更低的维护成本。

## 添加Cypress框架环境
#### 方式一、如果是本地运行，先将Cy目录下老的文件清空，自己进行重新安装。
步骤：
1、安装node.js
RUN wget https://nodejs.org/dist/v9.3.0/node-v9.3.0-linux-x64.tar.xz
RUN xz -d node-v9.3.0-linux-x64.tar.xz
RUN tar -xf node-v9.3.0-linux-x64.tar
RUN ln -s  /。。。/node-v9.3.0-linux-x64/bin/node  /usr/bin/node
RUN ln -s  /。。。/node-v9.3.0-linux-x64/bin/npm  /usr/bin/npm

2、安装Cypress
npm init 生成package.json文件
npm install -g cnpm --registry=https://registry.npm.taobao.org　　添加淘宝镜像
cnpm install cypress --save-dev

3、试运行、生成默认文件
npx cypress open

#### 方式二、使用镜像运行cypress/included
安装镜像
docker run -it -v $PWD:/e2e -w /e2e cypress/included:3.2.0
直接运行项目即可

前端代码：https://github.com/DeltaFarce/LaatUI_Vue
