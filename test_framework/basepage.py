# -*- coding: UTF-8 -*-
import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 初始化
    _driver: WebDriver =None
    _current_element: WebElement = None

    def start(self):
        caps ={
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True

        }
        self._driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self._driver.implicitly_wait(20)
    # 封装方法
    def stop(self):
        self._driver.quit()

    def find(self,locator):
        self._current_element=self._driver.find_element(*locator)
        return self
    def click(self):
        self._current_element.click()
        return self

    def sendkeys(self,text):
        self._current_element.send_keys(text)
        return self
    def back(self):
        self._driver.back()
        return self

    def go_run(self,po_method,**kwargs):
        with open('page_demo.yaml') as f:
            yaml_data=yaml.safe_load(f)
            """
            
            """
            # 遍历读取出来数据
            for step in yaml_data[po_method]:
                if isinstance(step,dict):
                    for key in  step.keys():
                        if key =='id':
                            locator=(By.ID,step[key])
                            self.find(locator)
                        elif key =='click':
                            self.click()
                        elif  key=='send_keys':
                            text=str(step[key])
                            #  kwargs.items()遍历字典中所有的key 以及value，返回“key，value"
                            for k,v in kwargs.items():
                                # self.sendkeys(text)
                                text =text.replace('${'+k+'}',v)
                                self.sendkeys(text)
                        else:
                            logging.error(f"dont know {step}")


