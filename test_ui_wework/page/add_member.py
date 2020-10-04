# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_ui_wework.page.basepage import BasePage
from test_ui_wework.page.contact_page import ContactPage


class AddMember(BasePage):

    def addmember(self,phone):
        self.find(By.ID,'username').send_keys("美少女战士2")

        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('998877662')
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        return ContactPage(self.driver)


