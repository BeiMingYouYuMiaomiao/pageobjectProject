# -*- coding: UTF-8 -*-
import yaml
from appium.webdriver import webdriver

from UI自动化测试框架.page.main_page import Main
from UI自动化测试框架.page.page_base import BasePage


class App(BasePage):
    _package='com.xueqiu.android'
    _activity='.view.WelcomeActivityAlias'
    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['noReset'] = 'true'
            desired_caps['dontStopAppOnReset'] = 'true'
            desired_caps['udid']=yaml.safe_load(open('../page/configuration.yaml'))['desired_caps']['udid']
            # 跳过安装
            desired_caps['skipDeviceInitialization'] = 'true'
            # 默认输入是英文输入，更改可以输入中文
            desired_caps['resetKeyBoard'] = 'true'

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
            self._driver.implicitly_wait(5)
        else:
            # desired_caps中的appPackage、appActivity
            # self._driver.launch_app()
            # 启动任何appPackage和appActivity
            self.driver.start_activity(self._package,self._activity)

        return self



    def restart(self):
        self._driver.close_app()
        self._driver.launch_app()

    def stop(self):
        self._driver.quit()

    def main(self) ->Main:
        return Main(self._driver)
