# -*- coding: UTF-8 -*-
from selenium  import webdriver
from selenium.webdriver.common.by import By

from test_ui_wework.page.add_member import AddMember
from test_ui_wework.page.basepage import BasePage
from test_ui_wework.page.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_contact(self):
        return ContactPage(self.driver)



    def goto_addmember(self):

        self.driver.find_element(By.CSS_SELECTOR,'[node-type="addmember"]').click()
        return AddMember(self.driver)