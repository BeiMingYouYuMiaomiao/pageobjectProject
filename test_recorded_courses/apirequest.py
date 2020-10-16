# -*- coding: UTF-8 -*-
import base64
import json

from requests import request


class ApiRequest:

    req_data={
        'method':'get',
        'url':'http://127.0.0.1:9999/demo1.txt',
        'headers':None,
        'encoding':'base64'
    }
    # request 二次封装
    def send(self,data:dict):
        req=request(data['method'],data['url'],headers=data['headers'])
        if data['encoding'] =='base64':
            return  json.loads(base64.b64decode(req.content))