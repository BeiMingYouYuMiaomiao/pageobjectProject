# -*- coding: UTF-8 -*-
# from test_appium.test_liveclass2.page.memberinvitepage import MemberInvitePage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_liveclass2.page.basepage import BasePage


class ContactAddPage(BasePage):

    # def __init__(self,driver):
    #     self.driver=driver
    name_ele=(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
    gender_ele_boy=(MobileBy.XPATH, "//*[@text='男']")
    gender_ele_girl=(MobileBy.XPATH, "//*[@text='女']")
    phone_ele=(MobileBy.ID, "com.tencent.wework:id/fiv")
    save_ele=(MobileBy.ID, "com.tencent.wework:id/hy0")
    def edit_name(self,name):
        # 选择姓名输入框，使用父节点方式定位，输入name
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)

        self.find_and_send(self.name_ele,name)
        return self
    def edit_gender(self,gender):
        # 选择性别，先点击后弹出选择文本
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.find_and_click(self.gender_ele_boy)
        #如果是男选择男，如果是女选择女
        sleep(3)
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
            self.find_and_click(self.gender_ele_boy)
        else:
            # self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
            self.find_and_click(self.gender_ele_girl)
        return self

    def edit_phonenum(self,phonenum):
        # 输入手机号码
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fiv").send_keys(phonenum)
        self.find_and_send(self.phone_ele,phonenum)
        return self

    def click_save(self):
        from test_appium.test_liveclass2.page.memberinvitepage import MemberInvitePage
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hy0").click()
        self.find_and_click(self.save_ele)
        return MemberInvitePage(self.driver)