# -*- coding: UTF-8 -*-
from test_appium.test_datadriver.page.basepage import BasePage
from test_appium.test_datadriver.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)