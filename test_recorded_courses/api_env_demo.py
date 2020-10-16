# -*- coding: UTF-8 -*-
import requests


class Api:
    env={
        'default':'test',
        'http://httpbin.testing-studio.com':{
            'dev':'127.0.0.1',
            'test':'127.0.0.2'
        }
    }


    def send(self,data:dict):
        # http://httpbin.testing-studio.com   修改default的value 就能切换接口地址
        data['url']=str(data['url']).replace('http://httpbin.testing-studio.com',self.env['http://httpbin.testing-studio.com'][self.env['default']])
        r=requests.request(method=data['method'],url=data['url'],headers=data['headers'],)
        return r