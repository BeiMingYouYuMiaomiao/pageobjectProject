# -*- coding: UTF-8 -*-
from selenium import webdriver


class TestH5Performance:
    def test_timing(self):
        driver=webdriver.Chrome()
        driver.get("http://baidu.com")
        # return JSON.stringify(要执行的JS语句) ，进行一个JSON格式化，再返回来
        timing=driver.execute_script("return JSON.stringify(window.performance.timing)")
        print(timing)