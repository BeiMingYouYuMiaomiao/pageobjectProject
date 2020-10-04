# -*- coding: UTF-8 -*-
from test_ui_wework.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        # 实例化主页面
        self.main = MainPage()
        # 从主页面跳转至添加成员页面，调用添加成员方法
        result = self.main.goto_addmember().addmember('13388889997').get_memberlist()
        assert '美少女战士2' in result

    def test_add_member1(self):
        # 从主页面跳转至通讯录页面，在跳转至添加成员页面，调用添加成员方法
       pass
    def test_add_member_error(self):
        # 实例化主页面
        self.main = MainPage()
        # 从主页面跳转至添加成员页面，调用添加成员方法
        result = self.main.goto_addmember().addmember('13388889!@').get_phone_error_message()

        assert '请填写正确的手机号码'==result
    def teardown(self):
        self.main.driver.quit()