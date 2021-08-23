# -*- coding: UTF-8 -*-
import requests

from 接口测试实战.weixin_api.base_api import BaseApi
from 接口测试实战.weixin_api.wework_utils import WeworkUtils


class AddressPage(BaseApi):

    def __init__(self):
        _corpsecret = 'Y0gDaB1xqsLzQKyVyEzxp59cBVWzd_iNUWR8WaUM6Lc'
        utils = WeworkUtils()
        token = utils.get_token(_corpsecret)
        self.params={'access_token':token}
    def get_member_info(self):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/get',
            'params': {

                'userid': 'meishaonv111'
            }
        }

        return self.send_api(data, self.params)

    def add_member(self):
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create',
            'json': {
                "userid": "meishaonv111",
                "name": "美少女111",
                "mobile": "13800000001",
                "department": [2]
            }
        }
        return self.send_api(data, self.params)

    """
    更新成员
    请求方式：POST（HTTPS）
    请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
    """

    def update_member(self):
        # data字典中 json 参数 只能叫做json才会被识别
        data = {
            'method': 'post',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/update',

            'json': {
                "userid": "meishaonv111",
                "name": "李四",
                "department": [2],
                "position": "后台工程师",
                "mobile": "13800000000"
            }
        }

        return self.send_api(data, self.params)

    """
    请求方式：GET（HTTPS）
    请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
    """

    def delete_member(self):
        data = {
            'method': 'get',
            'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/delete',
            'params': {

                'userid': 'meishaonv111'
            }
        }

        return self.send_api(data, self.params)
