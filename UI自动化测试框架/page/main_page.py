# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from UI自动化测试框架.page.page_base import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID,'tv_search').click()
        self.steps('../page/main.yml')

