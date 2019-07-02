# -*- coding: utf-8 -*-

try:
    import simplejson as json
except:
    import json

from flask import Flask, jsonify
from config import config
from todo import Todo
from monitor import Monitor
from flask_restful import Api
from .utils import prepare_json_response

import logging
from logging.handlers import RotatingFileHandler


def setup_log(log_level, config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=log_level)  # 根据配置类型设置日志等级

    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(config[config_name].LOG_PATH + config[config_name].LOG_FILENAME, maxBytes=1024 * 1024 * 100, backupCount=10,
                                           encoding='utf-8')
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(lineno)d - %(levelname)s - %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)
    setup_log(config[config_name].LOG_LEVEL, config_name)

    api.add_resource(Todo, '/todo')
    api.add_resource(Monitor, '/monitor')

    # 附加路由和自定义的错误页面
    @app.errorhandler(400)
    def bad_request(error):
        """
        Renders 400 response
        :returns: JSON
        :rtype: flask.Response
        """
        return jsonify(
            prepare_json_response(
                code=400,
                message="Error 400: Bad request",
                success=False,
                data=None
            )
        ), 400

    @app.errorhandler(401)
    def unauthorized(error):
        """
        Renders 400 response
        :returns: JSON
        :rtype: flask.Response
        """
        return jsonify(
            prepare_json_response(
                code=401,
                message="Error 401: Unauthorized",
                success=False,
                data=None
            )
        ), 401

    @app.errorhandler(403)
    def permission_error(error):
        """
        Renders 403 response
        :returns: JSON
        :rtype: flask.Response
        """
        return jsonify(
            prepare_json_response(
                code=403,
                message="Error 403: Permission Denied",
                success=False,
                data=None
            )
        ), 403

    @app.errorhandler(404)
    def page_not_found(error):
        """
        Renders 404 response
        :returns: JSON
        :rtype: flask.Response
        """
        return jsonify(
            prepare_json_response(
                code=404,
                message="Error 404: Item Not Found",
                success=False,
                data=None
            )
        ), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        """
        Renders 405 response
        :returns: JSON
        :rtype: flask.Response
        """
        return jsonify(
            prepare_json_response(
                code=405,
                message="Error 405: Method not allowed",
                success=False,
                data=None
            )
        ), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Renders 400 response
        :returns: JSON
        :rtype: flask.Response
        """

        return jsonify(
            prepare_json_response(
                code=500,
                message="Error 500: Internal server error",
                success=False,
                data=None
            )
        ), 500

    return app
