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

    # 实际情况PO页面会很多，那一个页面配置一个配置文件很不现实
    """
    PO数据驱动设计思想:
    如果我测试新的PO页面，就要创建新的PO页面，在测试时调用里面的方法，那么就要读取的测试数据与测试步骤数据
    
    """
    def __init__(self,po_file=None):
        # 如果参数不为空，则定义一个 self.po_file （不知道怎么说，后面要学习Python） 存起来
        if po_file is not None:
            # 继承basepage的类初始化时这个变量
            self._po_file=po_file
    @classmethod
    def start(cls):
        caps ={
            'platformName': 'android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.xueqiu.android',
            'appActivity': '.view.WelcomeActivityAlias',
            'noReset': True

        }
        cls._driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        cls._driver.implicitly_wait(20)
        return cls
    # 封装方法
    def stop(self):
        BasePage._driver.quit()

    def find(self,locator):
        if locator[0] == 'text':
            locator_new=(By.XPATH, f'//*[contains(@text,"{locator[1]}")]')

        else:
            """self._current_element = self._driver.find_element(By.ID)
            
            class By(object):
                    ID = "id"
                    XPATH = "xpath"
                    LINK_TEXT = "link text"
                    PARTIAL_LINK_TEXT = "partial link text"
                    NAME = "name"
                    TAG_NAME = "tag name"
                    CLASS_NAME = "class name"
                    CSS_SELECTOR = "css selector"
            """
            locator_new = locator

        self._current_element=BasePage._driver.find_element(*locator_new)
        return self
    def click(self):
        self._current_element.click()
        return self

    def sendkeys(self,text):
        self._current_element.send_keys(text)
        return self


    def go_run(self,po_method,**kwargs):
        with open(self._po_file) as f:
            yaml_data=yaml.safe_load(f)
            """
            
            """
            # 遍历读取出来数据
            print(yaml_data[po_method])
            for step in yaml_data[po_method]:
                if isinstance(step,dict):
                    for key in step.keys():
                        if key in ['id', 'aid', 'text']:
                            locator=(key,step[key])

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


