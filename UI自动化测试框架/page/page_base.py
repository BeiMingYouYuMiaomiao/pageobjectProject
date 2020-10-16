# -*- coding: UTF-8 -*-
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 将driver定义为一个实例变量，这样BasePage的子类就可以用了
    _driver:WebDriver
    def __init__(self,driver:WebDriver=None):
        self._driver =driver

    def find(self,locator,value):
        return  self._driver.find_element(locator,value)
    def click(self,locator,value):
        self.find(locator,value).click()

    def steps(self,path):
        with open(path) as f:
            steps=yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element=self.find(step['by'],step['locator'])
                if "action" in step.keys():
                    action =step['action']
                    if action=='click':
                        element.click()
