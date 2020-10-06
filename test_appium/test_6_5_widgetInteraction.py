# -*- coding: UTF-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestWidgetInteraction:
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

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        print('搜索测试')
        """
        1、打开雪球app
        2.点击搜索输入框
        3.输入阿里巴巴，点击查询
        4.获取这只上香港 阿里巴巴的股价，并判断这只股价>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']").click()
        current_price=float(self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text)
        assert current_price > 280
    def test_attr(self):
        el = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = el.is_enabled()
        print(el.text)
        print(el.location)
        print(el.size)
        if search_enabled == True:
            el.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
            alibaba_ele =self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and@text='阿里巴巴']")
            ele_displayed = alibaba_ele.get_attribute("displayed")
            if ele_displayed == 'true':
                print("成功")
            else:
                print("失败")


    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 获取屏幕的宽和高
        window_rect = self.driver.get_window_rect()
        print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        xw =float(width/2)
        y_start=float(height*4/5)
        y_end=float(height*1/5)
        # action.press(x=353,y=1266).wait(200).move_to(x=353,y=295).release()
        action.press(x=xw, y=y_start).wait(2000).move_to(x=xw, y=y_end).release().perform()
    if __name__ == '__main__':
        pytest.main()