# -*- coding: utf-8 -*-


import os
import sys
import logging
from flask_restful import Resource, reqparse
from .utils import prepare_json_response
from config import config

reload(sys)
sys.setdefaultencoding('utf-8')

cfg = config[os.getenv('FLASK_CONFIG') or 'default']


class Todo(Resource):
    parser = reqparse.RequestParser()  # must enter name、age and sex.
    parser.add_argument('country', type=str, required=True, help='This field can be country name:china or england.')
    parser.add_argument('province', type=str, required=True, help='Must enter the province of the country.')
    parser.add_argument('city', type=str, required=True, help='This field can be city name:shanghai or suzhou.')
    parser.add_argument('Token', location='headers')

    def get(self):
        return 'OK', 200

    def post(self):

        data = Todo.parser.parse_args()
        country = data['country']
        province = data['province']
        city = data['city']
        token = data['Token']

        if token == cfg.TOKEN:
            logging.info('当前token为 %s' % (token))
        elif token == None:
            return prepare_json_response(
                code=10,
                success=False,
                message="token 不能为空!",
                data=None
            )
        else:
            return prepare_json_response(
                code=11,
                success=False,
                message="token 不正确，请联系管理员!",
                data=None
            )

        resultList = []

        logging.info("Get a post request, country=%s, province=%s, city=%s" % (country, province, city))

        if country in ['china', 'england']:
            # 针对一个地区进行修改
            data = cfg.data['info'][country]
            if isinstance(data, dict):
                # item = jiangsu/zhejiang/sichuan
                for item in data:

                    if isinstance(data[item], dict):
                        if province == 'jiangsu':
                            # do something
                            logging.info("Get a post request, province=%s" % province)
                        elif province == 'zhejiang':
                            # do something
                            logging.info("Get a post request, province=%s" % province)
                        else:
                            return prepare_json_response(
                                code=404,
                                success=False,
                                message="Error 404: %s Is Not Exist" % province,
                                data=None
                            )
                    else:
                        return prepare_json_response(
                            code=-1,
                            success=False,
                            message="Json parse failed!",
                            data=None
                        )

                return resultList
            else:
                return prepare_json_response(
                    code=-1,
                    success=False,
                    message="Json parse failed!",
                    data=None
                )
        else:
            return prepare_json_response(
                    code=404,
                    success=False,
                    message="Error 404: %s Is Not Exist" % country,
                    data=None
                )




