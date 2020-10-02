# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from page1.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID, 'corp_name').send_keys('name1')
        self.find(By.ID, 'manager_name').send_keys('name2')
        return True
