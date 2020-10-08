# -*- coding: UTF-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSeniorPosition:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 不清楚上一次的'记录'
        desired_caps['noReset'] = 'true'
        # 执行用例后，不退出
        desired_caps['dontStopAppOnReset'] = 'true'
        # 跳过安装
        desired_caps['skipDeviceInitialization'] = 'true'
        # 默认输入是英文输入，更改可以输入中文
        desired_caps['resetKeyBoard'] = 'true'
        # 使用的是uiautomator2工作引擎，默认使用的也是这个引擎
        desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()
    # 通过父节点找到具体的子节点
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # 可以使用lamda表达式
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))

        # price=self.driver.find_element(*locator).text
        print(ele.text)
