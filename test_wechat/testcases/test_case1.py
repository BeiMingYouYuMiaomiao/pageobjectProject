# -*- coding: UTF-8 -*-
from time import sleep

from selenium.webdriver.common.by import By

from test_wechat.page.main_page import Main


class TestCase:
    def teardown(self):
        self.main.driver.quit()
    def test_addmember(self):
        self.main=Main()
        result = self.main.goto_addmember().add_member().get_memberlist()
        assert '水冰月'in result

    def test_adddepartment(self):
        self.main=Main()
        self.main.goto_contact().add_department()
        depart_names = self.main.goto_contact().get_department_name()
        assert '我是部门1'in depart_names
    def test_importcontact(self):
        self.main = Main()
        self.importcontact=self.main.goto_importcontact()
        self.importcontact.import_contact()
        text = self.importcontact.get_text()
        assert 'test.xlsx' == text

