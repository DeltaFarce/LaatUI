FROM python:3.6.7
RUN mkdir /Laat
WORKDIR /Laat
COPY . /Laat/
RUN python -m pip install --upgrade pip
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt

# 安装node环境
RUN wget http://nodejs.org/dist/v0.10.24/node-v0.10.24.tar.gz
RUN tar zxvf node-v0.10.24.tar.gz
RUN cd node-v0.10.24
RUN ./configure --prefix=/usr/local/node/0.10.24
RUN make
RUN make install
RUN ln -s  /Laat/nodejs/bin/npm  /usr/local/bin/
RUN ln -s  /Laat/nodejs/bin/node  /usr/local/bin/

RUN pip install gunicorn
RUN celery -A LaatUI worker -l info
RUN celery -A LaatUI flower
EXPOSE 80
CMD gunicorn LaatUI.wsgi -w 2 -k gthread -b 0.0.0.0:80