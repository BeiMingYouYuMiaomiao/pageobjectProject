# -*- coding: UTF-8 -*-
from test_recorded_courses import api_env_demo


def test_send():
    data={
        'method':'get',
        'headers':None,
        'url':'http://httpbin.testing-studio.com'
    }
    r=api_env_demo.Api().send(data).text
    print(r)

