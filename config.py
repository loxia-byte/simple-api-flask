# -*- coding: utf-8 -*-


import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2vym+ky!97d5kc64mnz06y1mui3lut#(^wd=%s_qj$1%x'


class DevelopmentConfig(Config):
    DEBUG = True

    host = '0.0.0.0'
    TOKEN = '67x9UzVcFDgZ4hdev'
    JSON_AS_ASCII = True

    LOG_PATH = 'logs/'
    LOG_FILENAME = 'apps_dev.log'
    LOG_LEVEL = 'INFO'
    data = {
        "info": {
            "china": {
                "jiangsu": {
                    "suzhou": 100
                    }
                }
        }
    }


class TestingConfig(Config):
    LOG_PATH = 'logs/'
    LOG_FILENAME = 'apps_test.log'
    LOG_LEVEL = 'INFO'

    TOKEN = 'Cy2mBP48n9KbxYqa'
    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    data = {
        "info": {
            "china": {
                "jiangsu": {
                    "nanjing": 80
                }
            }
        }
    }


class ProductionConfig(Config):
    LOG_PATH = 'logs/'
    LOG_FILENAME = 'apps_prod.log'
    LOG_LEVEL = 'INFO'
    TOKEN = 'M6vYz644eWfj2VAtYZh2pro'

    if not os.path.exists(LOG_PATH):
        os.makedirs(LOG_PATH)

    data = {
        "info": {
            "china": {
                "zhejiang": {
                    "hangzhou": 90
                }
            },
            "england": {
                "london": {
                    "abc": 95
                }
            }
        }
    }


config = {
    'dev': DevelopmentConfig,
    'qa': TestingConfig,
    'pro': ProductionConfig,
    'default': DevelopmentConfig
}