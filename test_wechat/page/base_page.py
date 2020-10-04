# -*- coding: UTF-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    _url = ""

    def __init__(self,driver : WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            #隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self._url != '':
            self.driver.get(self._url)


    def find(self,by,locator):
        return  self.driver.find_element(by,locator)