# -*- coding: UTF-8 -*-
from 接口测试实战.weixin_api.address_page import AddressPage


class TestApi:
    def setup(self):
        self.addresspage = AddressPage()

    def test_add_member(self):
        t=self.addresspage.add_member()
        assert t['errcode'] ==0

    def test_getmember_info(self):
        t=self.addresspage.get_member_info()
        assert t['errcode'] == 0
    def test_update_member(self):
        t=self.addresspage.update_member()
        assert t['errcode'] ==0
    def test_delete_member(self):
        t=self.addresspage.delete_member()
        assert t['errcode'] ==0

