# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
     _base_url = ""
     def __init__(self,driver_base: WebDriver=None):
         if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)

            self.driver.implicitly_wait(5)

         else:
            self.driver = driver_base

         if self._base_url != "":
            self.driver.get(self._base_url)

     def find(self,by,locator):
        return self.driver.find_element(by,locator)