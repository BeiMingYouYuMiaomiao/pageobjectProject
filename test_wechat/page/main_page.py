# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from test_wechat.page.add_member_page import AddMember
from test_wechat.page.base_page import BasePage
from test_wechat.page.contact_page import Contact
from test_wechat.page.import_contact_page import ImportContact


class Main(BasePage):

    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_contact(self):
        self.find(By.LINK_TEXT,'通讯录').click()
        return Contact(self.driver)


    def goto_addmember(self):
        self.find(By.CSS_SELECTOR, '[node-type="addmember"]').click()
        return AddMember(self.driver)

    def goto_importcontact(self):
        self.find(By.CSS_SELECTOR,'.ww_indexImg_Import').click()
        return ImportContact(self.driver)