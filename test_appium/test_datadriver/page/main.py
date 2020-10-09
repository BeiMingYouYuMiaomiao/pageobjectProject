# -*- coding: UTF-8 -*-
from test_appium.test_datadriver.page.basepage import BasePage
from test_appium.test_datadriver.page.market import Market


class Main(BasePage):
    def goto_market(self):
        # 数据驱动会在testcases文件夹中执行驱动，所以要先去testcases的上一层目录的page目录中
        self.steps("../page/main.yaml")
        return Market(self._driver)