# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


from test_wechat.page.base_page import BasePage
from test_wechat.page.contact_page import Contact


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID,'username').send_keys('水冰月')
        self.find(By.ID,'memberAdd_acctid').send_keys('9988776601')
        self.find(By.ID,'memberAdd_phone').send_keys('13681466630')
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

        return Contact(self.driver)

