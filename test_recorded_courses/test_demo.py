# -*- coding: UTF-8 -*-
import pystache
import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth
import base64
import json
class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get', auth=('user', 'pass'))
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code ==200


    def test_query(self):
        payload={
            "level":"1",
            "name":"miaomiao"
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        """Sends a POST request.

            :param url: URL for the new :class:`Request` object.
            :param data: (optional) Dictionary, list of tuples, bytes, or file-like
                object to send in the body of the :class:`Request`.
            :param json: (optional) json data to send in the body of the :class:`Request`.
            :param \*\*kwargs: Optional arguments that ``request`` takes.
            :return: :class:`Response <Response>` object
            :rtype: requests.Response
            """
        payload={
            "level":"1",
            "name":"miaomiao"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200
    def test_post_json(self):

        payload={
            "level":"1",
            "name":"miaomiao"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200




    def test_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get', headers={'H':'header_id'})
        print(r.text)
        print(r.json())
        print(r.status_code)
        print(r.headers)
        assert r.json()['headers']['H'] == 'header_id'


    def test_pystache(self):
        print(pystache.render('hell{{username}}!!', {'username': 'miaomiao'}))

    def test_jsonpath(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        # print(r.text)
        """traverse JSON object using jsonpath expr, returning values or paths"""
        print(jsonpath(r.json(),'$..name')[0])
        # hamcrest
        assert_that(jsonpath(r.json(),'$..name')[0],equal_to('社区治理'))

    def test_get_cookie1(self):
        r = requests.get('https://home.testing-studio.com/cookies')
        print(r.text)
        print(r.cookies)

    def test_get_cookie2(self):
        header={'Cookie':'testcookies',
                'User-Agent':'beimingyouyumiaomiao'

                }
        r = requests.get('http://httpbin.testing-studio.com/cookies',headers=header)

        print(r.request.headers)

    def test_auth(self):

        r = requests.get('http://httpbin.testing-studio.com/basic-auth/qwe6/123',auth=HTTPBasicAuth("qwe6","123"))
        print(r)
    def test_encode(self):
        r = requests.get("http://127.0.0.1:9999/demo1.txt")
        print(json.loads(base64.b64decode(r.content)))

