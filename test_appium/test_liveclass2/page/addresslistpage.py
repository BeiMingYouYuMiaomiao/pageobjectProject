# -*- coding: UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_liveclass2.page.basepage import BasePage
from test_appium.test_liveclass2.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    addmember_text='添加成员'
    def add_member(self):
        # 进入通讯录页面，点击成员
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.find_by_scroll_and_click(self.addmember_text)
        return MemberInvitePage(self.driver)