# -*- coding: UTF-8 -*-
from appium import webdriver

from test_appium.test_datadriver.page.basepage import BasePage
from test_appium.test_datadriver.page.main import Main


class App(BasePage):
    def start(self):
        _package="com.xueqiu.android"
        _activity=".view.WelcomeActivityAlias"
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = _package
            desired_caps['appActivity'] = _activity
            desired_caps['autoGrantPermissions'] = True

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package,_activity)
        return  self

    def main(self):
        return  Main(self._driver)
