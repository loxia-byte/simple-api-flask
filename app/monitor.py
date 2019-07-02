# -*- coding: utf-8 -*-

from flask_restful import Resource


class Monitor(Resource):
    def get(self):
        return 1, 200
