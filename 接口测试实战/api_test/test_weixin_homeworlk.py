# -*- coding: UTF-8 -*-
"""
获取access_token
请求方式：GET（HTTPS）
请求URL：https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
"""
import requests

corpid='ww5fcfd4d37ecb1852'
corpsecret='Y0gDaB1xqsLzQKyVyEzxp59cBVWzd_iNUWR8WaUM6Lc'
def get_token():
    url=f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
    r=requests.get(url)
    result=r.json()
    token = result['access_token']
    return token
"""
创建部门
请求方式：POST（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN
"""

def test_creatdepartment():
    token=get_token()
    url=f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token}'
    data={
       "name": "广州研发中心",
       "name_en": "RDGZ",
       "parentid": 1,
       "order": 1,
       "id": 4
    }
    r=requests.post(url,json=data)
    print(r.json())

"""
更新部门
请求方式：POST（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=ACCESS_TOKEN
"""
def test_updatedepartment():
    token=get_token()
    url=f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token}'
    data={
       "id": 4,
       "name": "北京研发中心",
       "name_en": "RDGZ",
       "parentid": 1,
       "order": 1
}
    r=requests.post(url,json=data)
    print(r.json())

"""
获取部门列表
请求方式：GET（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=ACCESS_TOKEN&id=ID
"""
def test_getdepartmentlist():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}'
    r =requests.get(url)
    print(r.json())

"""
删除部门
请求方式：GET（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=ACCESS_TOKEN&id=ID
"""
def test_deletedepartment():
    token = get_token()
    url = f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id=4'
    r=requests.get(url)
    print(r.json())