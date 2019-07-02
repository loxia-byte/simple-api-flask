# -*- coding: utf-8 -*-

"""
simple-api-flask.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within simple-api-flask
that are also useful for external consumption.
"""


from .structures import CaseInsensitiveDict
from .__version__ import __version__


def prepare_json_response(code, success, message, data):
    response = {"code": 200, "success": success}
    if code:
        response["code"] = code

    if data:
        response["data"] = data
        response["data_count"] = len(data)

    if message:
        response["message"] = message
    return response


def default_user_agent(name="simple-api-flask"):
    """
    Return a string representing the default user agent.

    :rtype: str
    """
    return '%s/%s' % (name, __version__)


def default_headers():
    """
    :rtype: requests.structures.CaseInsensitiveDict
    """
    return CaseInsensitiveDict({
        'User-Agent': default_user_agent(),
        'Accept-Encoding': ', '.join(('gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
    })