# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestLivingClassOne:
    # 定义setup，预制信息，连接appium服务
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
    # teardown 用例执行后，关闭driver
    def teardown(self):
        self.driver.quit()

    #  测试添加成员

    def test_addmember(self):
        # 定义添加成员内容
        name = '甜瓜'
        gender = '男'
        phonenum='13681466630'
        # 进入首页后，点击下方'通讯录'
        # el1=self.driver.find_element_by_xpath("//*[@text='通讯录']")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        # 进入通讯录页面，点击成员
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        # 进入选择添加方式页面，选择手动添加
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        # 选择姓名输入框，使用父节点方式定位，输入name
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # 选择性别，先点击后弹出选择文本
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # 如果是男选择男，如果是女选择女
        sleep(3)
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        # 输入手机号码
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fiv").send_keys(phonenum)
        # 点击保存
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hy0").click()
        # 保存后，根据页面布局获取toast文本，可进行断言
        toastmessage = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text

        print(toastmessage)


    def test_deletemember(self):
        # 进入首页后，点击下方'通讯录'
        # 首页点击下方 通讯录
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 进入通讯录页面后，点击搜索
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hxw').click()
        # 输入要删除的联系人"甜瓜"
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ghu').send_keys('甜瓜')
        # 在搜索结果的列表中选中
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/dkf').click()
        # 选择右上方 ...
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hxm').click()
        # 选择编辑
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/b91').click()
        # 选择删除
        self.driver.find_element(MobileBy.XPATH,'//*[@text="删除成员"]').click()

       # 选择确认删除
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/bjp').click()
        mes =self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ca0').text

        # print(mes)
        assert  "无搜索结果" == mes