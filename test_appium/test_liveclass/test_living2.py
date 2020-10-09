# -*- coding: UTF-8 -*-
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

def get_member():
    with open('./datas/member.yaml') as f:
        datas =yaml.safe_load(f)
        return datas

class TestLivingClassOne:

    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        # desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
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
    def test_qiyeweixin_sendmessage(self):
        self.driver.find_element_by_id("com.tencent.wework:id/hxw").click()

        self.driver.find_element_by_id("com.tencent.wework:id/ghu").send_keys("11")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        el4.click()
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/ejs")

        el5.send_keys("hello word")
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/ejo")
        el6.click()



    @pytest.mark.parametrize('name,gender,phonenum',get_member())
    def test_addmember(self,name,gender,phonenum):
        # name = '甜瓜'
        # gender = '男'
        # phonenum='13681466630'
        # el1=self.driver.find_element_by_xpath("//*[@text='通讯录']")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()

        if gender == '男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fiv").send_keys(phonenum)

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hy0").click()

        toastmessage = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text

        print(toastmessage)


