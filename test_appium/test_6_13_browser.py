# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['browserName'] = 'Browser'

        # 不清楚上一次的'记录'
        desired_caps['noReset'] = 'true'
        # 可以使用默认的路径下的chromedriver /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver
        # 也可以指定一个地址
        # desired_caps['chromedriverExecutable'] = ''

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()
        sleep(5)



