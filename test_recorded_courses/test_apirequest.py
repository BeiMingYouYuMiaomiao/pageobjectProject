# -*- coding: UTF-8 -*-
from test_recorded_courses import apirequest

class TestApi:
    req_data = {
        'method': 'get',
        'url': 'http://127.0.0.1:9999/demo1.txt',
        'headers': None,
        'encoding': 'base64'
    }
    def test_send(self):

        print(apirequest.ApiRequest().send(self.req_data))

