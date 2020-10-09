# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        # desired_caps['deviceName'] = 'emulator-5554'
        #adb shell dumpsys window|grep mCurrent   获取APP及首页名字
        desired_caps['appPackage']= 'com.xueqiu.android'
        desired_caps['appActivity'] = '.common.MainActivity'
        # desired_caps['browserName'] = 'Browser'
        # 跳过安装
        desired_caps['skipDeviceInitialization'] = 'true'
        # 不清楚上一次的'记录'
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        pass

    def test_webview(self):
        # 点击"交易"
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        A_locator = (MobileBy.XPATH,'//*[@id="app"]/div/div/div/ul/li[1]/div[2]/h1')
        print(self.driver.contexts)
        # 一般情况下，context的最后一个是新打开的页面  但是也有特殊情况，是乱的 可以遍历处理
        # 从原生view 切换至 webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击 A股开户
        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        # print(self.driver.window_handles)
        # print(self.driver.current_window_handle)
        # 进入开户页面
        # KH_window = self.driver.window_handles[-1]
        # print(self.driver.current_window_handle)
        # self.driver.switch_to.window(KH_window)

        phonenumber_locator = (MobileBy.ID,"phone-number")
        # 显示等待
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        # 输入手机号码
        self.driver.find_element(*phonenumber_locator).send_keys("13810104245")
        self.driver.find_element(MobileBy.ID,"code").send_keys("123456")
        self.driver.find_element(MobileBy.CLASS_NAME,"btn-submit").click()