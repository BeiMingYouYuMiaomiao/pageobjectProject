# -*- coding: UTF-8 -*-
"""
App类：
    app


"""
from appium import webdriver

from test_appium.test_liveclass2.page.basepage import BasePage
from test_appium.test_liveclass2.page.mainpage import MainPage


class App(BasePage):


    def start(self):
        if self.driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.tencent.wework'
            # desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
            desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
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
        else:
            # desired_caps中的appPackage、appActivity
            self.driver.launch_app()
            # 启动任何appPackage和appActivity
            #  self.driver.start_activity()

        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()
    """
    已经在start方法里实例化了一个driver
    直接传给MainPage       MainPage的接收需要创建一个init   

    
    """
    def goto_main(self) ->MainPage:
        return MainPage(self.driver)