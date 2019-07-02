#!/bin/bash

if [ $ENV == "product" ];then
    export FLASK_CONFIG='pro'
elif [ $ENV == "qa" ];then
    export FLASK_CONFIG='qa'
else
    export FLASK_CONFIG='default'
fi

/usr/sbin/nginx -c /etc/nginx/nginx.conf

cd /usr/local/simple-api-flask
gunicorn -c gunicorn.conf manage:app -t 6000 --pid /tmp/gunicorn.pid  --log-level info