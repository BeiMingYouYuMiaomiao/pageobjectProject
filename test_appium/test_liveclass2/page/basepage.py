# -*- coding: UTF-8 -*-

"""
基类：存放一些最基本的方法
实例化 driver find back home....

"""
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver


    # locator是一个元组
    def find(self,locator):
        return  self.driver.find_element(*locator)

    def find_and_click(self,locator):
        self.find(locator).click()

    # new UiSelector().scrollable(true).instance(0).scrollIntoView(new UiSelector().text(“WebView”).instance(0)

    def find_by_scroll_and_click(self,text):
        scroll_element =(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0))')
        self.find(scroll_element).click()
    def find_and_send(self,locator,content):
        self.find(locator).send_keys(content)

    def get_toast_text(self):
        toasttext=self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toasttext