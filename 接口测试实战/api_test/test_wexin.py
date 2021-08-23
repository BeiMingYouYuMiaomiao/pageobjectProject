# -*- coding: UTF-8 -*-
import requests

corpid='ww5fcfd4d37ecb1852'
corpsecret='Y0gDaB1xqsLzQKyVyEzxp59cBVWzd_iNUWR8WaUM6Lc'
def get_token():
    url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    r=requests.get(url)
    result=r.json()
    return result['access_token']


def test_getmember():
    token=get_token()
    print(token)
    url=f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=zhangsan'
    r = requests.get(url)
    print(r.json())

def test_addmember():
    token=get_token()
    url= f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    data={
        "userid": "meishaonv111",
        "name": "美少女111",
        "mobile": "13800000001",
        "department": [2]
    }
    r=requests.post(url,json=data)
    print(r.json())