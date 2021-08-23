# -*- coding: UTF-8 -*-
import requests

from 接口测试实战.weixin_api.base_api import BaseApi


class WeworkUtils(BaseApi):


    def get_token(self,corpsecret,corpid = 'ww5fcfd4d37ecb1852'):
        data={
            'method':'get',
            'url':'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            'params':{
                'corpid' : corpid,
                'corpsecret':corpsecret
            }
        }

        result = requests.request(**data).json()
        print(result)
        return result['access_token']