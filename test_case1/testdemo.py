# -*- coding: UTF-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options


class TestDemo:
    def setup(self):

        chrome_options = Options()
        chrome_options.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=chrome_options,executable_path='/Users/yuxin/Documents/tools/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_1(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium学习方法')
        self.driver.find_element_by_id('su').click()
        sleep(4)