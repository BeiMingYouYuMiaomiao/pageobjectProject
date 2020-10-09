# -*- coding: UTF-8 -*-
from appium import *
from appium.webdriver import webdriver
from selenium.webdriver import DesiredCapabilities

"""
小程序自动化的关键步骤：
    设置chromedriver正确版本
    设置chrome option 传递给chromedriver
    使用adb proxy 解决fix chromedriver 的bug

为什么有些手机无法自动化微信小程序
    低版本的Chromedriver在高版本的手机上有bug
    Chromedriver与微信定制的Chrome内核实现上有问题
解决方案： fix it
 chromedriver没有使用adb命令，而是使用了adb协议
 参考课程中提到的adb proxy源代码
"""
class TestMiniProgram:
    def setup(self):
        # 第一步 设置chromedriver正确版本
        # 简单粗暴的解决方案
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.common.MainActivity'
        # 不清楚上一次的'记录'
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyboard'] ='true'
        desired_caps['resetKeyboard'] = 'true'

        # desired_caps['chromedriverExecutable'] = ''  我使用默认的路径
        desired_caps['chromeOptions'] ={'androidProcess':''}
        desired_caps['abdPort'] = 5038

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

