# -*- coding: UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_liveclass2.page.basepage import BasePage
from test_appium.test_liveclass2.page.contactasddpage import ContactAddPage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver
    addmember_menual_element=(MobileBy.XPATH, "//*[@text='手动输入添加']")
    def addmember_menual(self):
        # 进入选择添加方式页面，选择手动添加
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.addmember_menual_element)
        return ContactAddPage(self.driver)

    def get_toast(self):
        # 保存后，根据页面布局获取toast文本，可进行断言
        # toastmessage = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        toastmessage = self.get_toast_text()
        print(toastmessage)

        return toastmessage