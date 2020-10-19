# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from test_new_framework.basepage import BasePage


class PageDemo(BasePage):
    # 页面内可操作性的功能

    def search(self,keywords):
        self.go_run('search',keyword=keywords)
        return self

    def back(self):
        self.po_run('back')
        return self

