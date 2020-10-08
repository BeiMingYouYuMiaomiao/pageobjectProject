# -*- coding: UTF-8 -*-
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
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
        # desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()

        # self.driver.quit()
    # 参数化的参数变量名要一致
    @pytest.mark.parametrize('searchkey,type,price',[('alibab','BABA',300),('XIAOMI','01810',22)])
    def test_search_parameterizition(self,searchkey,type,price):
        # 在首页，点击搜索框
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        # 在搜索框中输入内容
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # 选择搜出的结果下拉框第一个
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name']").click()
        #  注意字符串中变量的使用 字面量
        current_price = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        expect_price= price
        # 这块要注意  将获取的价格和预期价格都要转换为float，要不会报错
        current_price=float(current_price)
        expect_price=float(expect_price)
        assert_that(current_price,close_to(expect_price,expect_price*0.1))

    @pytest.mark.parametrize('searchkey,type,price', yaml.safe_load(open('./search_parameter.yaml')))
    def test_search_parameterizition1(self, searchkey, type, price):
        # 在首页，点击搜索框
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        # 在搜索框中输入内容
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        # 选择搜出的结果下拉框第一个
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name']").click()
        #  注意字符串中变量的使用 字面量
        current_price = self.driver.find_element(MobileBy.XPATH,
                                                 f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        expect_price = price
        # 这块要注意  将获取的价格和预期价格都要转换为float，要不会报错
        current_price = float(current_price)
        expect_price = float(expect_price)
        assert_that(current_price, close_to(expect_price, expect_price * 0.1))