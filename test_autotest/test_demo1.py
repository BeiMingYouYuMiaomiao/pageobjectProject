# -*- coding: UTF-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Test_Hogwars():
    def setup(self):
        #chrome_options = Options()
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()


    def test_hogwars(self):
        self.driver.get("https://testerhome.com/")

        self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element_by_link_text('Appium 中文文档小组').click()
        time.sleep(3)
       # self.driver.find_element_by_link_text('Appium 文档翻译计划 2020 启动 ，有兴趣参与的同学，请跟帖~').click()
        self.driver.find_element_by_class_name('node').click()
        time.sleep(3)