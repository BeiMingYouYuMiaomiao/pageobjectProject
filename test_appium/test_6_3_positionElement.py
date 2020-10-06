# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver

desired_caps={}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
# 不清楚上一次的'记录'
desired_caps['noReset'] = 'true'
# 执行用例后，不退出
desired_caps['dontStopAppOnReset'] = 'true'
# 跳过安装
desired_caps['skipDeviceInitialization'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('alibaba')

driver.quit()

