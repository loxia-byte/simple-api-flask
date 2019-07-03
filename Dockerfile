FROM python_nginx_gunicorn
COPY simple-api-flask.zip /usr/local/
RUN pip install flask flask-restful pyDes gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && unzip /usr/local/simple-api-flask.zip -d /usr/local/simple-api-flask \
    && mkdir /script
COPY startup.sh /script/startup.sh
COPY simple-api-flask.conf /etc/nginx/conf.d/simple-api-flask.conf
RUN chmod +x /script/startup.sh
USER root
WORKDIR /usr/local/simple-api-flask
CMD /script/startup.sh