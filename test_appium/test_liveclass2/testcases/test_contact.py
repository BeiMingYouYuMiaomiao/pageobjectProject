# -*- coding: UTF-8 -*-
import pytest
import yaml

from test_appium.test_liveclass2.page.app import App

def get_member():
    with open('../data1s/member.yaml') as f:
        datas =yaml.safe_load(f)
        return datas

class TestWeixin:


    def setup(self):
        self.app=App()

        self.main=self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', get_member())
    def test_addcontact(self,name,gender,phonenum):
        mypage= self.main.goto_addresslist().add_member().addmember_menual().edit_name(name).edit_gender(gender).edit_phonenum(phonenum).click_save()

        mytoast = mypage.get_toast()
        assert "添加成功" ==mytoast