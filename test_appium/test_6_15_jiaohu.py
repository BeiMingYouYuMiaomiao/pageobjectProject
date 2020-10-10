# -*- coding: UTF-8 -*-
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestJiaohu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 不清楚上一次的'记录'
        desired_caps['noReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        # 使用模拟器 emulator -list-avds
        # desired_caps['avd'] ='模拟器'
        # 跳过安装
        desired_caps['skipDeviceInitialization'] = 'true'
        # 默认输入是英文输入，更改可以输入中文
        desired_caps['resetKeyBoard'] = 'true'
        # 使用的是uiautomator2工作引擎，默认使用的也是这个引擎
        # desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # 模拟打电话
        self.driver.make_gsm_call('13810104245',GsmCallActions.CALL)
        # 模拟发短信
        self.driver.send_sms('13681466630','this is a message')
        # 模拟网络连接
        def set_network_connection(self: T, connection_type: int) -> int:
            """Sets the network connection type. Android only.

            Possible values:

                +--------------------+------+------+---------------+
                | Value (Alias)      | Data | Wifi | Airplane Mode |
                +====================+======+======+===============+
                | 0 (None)           | 0    | 0    | 0             |
                +--------------------+------+------+---------------+
                | 1 (Airplane Mode)  | 0    | 0    | 1             |
                +--------------------+------+------+---------------+
                | 2 (Wifi only)      | 0    | 1    | 0             |
                +--------------------+------+------+---------------+
                | 4 (Data only)      | 1    | 0    | 0             |
                +--------------------+------+------+---------------+
                | 6 (All network on) | 1    | 1    | 0             |
                +--------------------+------+------+---------------+
            """
        self.driver.set_network_connection()