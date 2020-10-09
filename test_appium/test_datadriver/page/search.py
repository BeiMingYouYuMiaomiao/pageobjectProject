# -*- coding: UTF-8 -*-
from test_appium.test_datadriver.page.basepage import BasePage


class Search(BasePage):
    def search(self,value):
        self._parameter["value_key"] = value
        self.steps("../page/search.yaml")