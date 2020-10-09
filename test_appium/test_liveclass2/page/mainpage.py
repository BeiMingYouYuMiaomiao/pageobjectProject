# -*- coding: UTF-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_liveclass2.page.addresslistpage import AddressListPage
from test_appium.test_liveclass2.page.basepage import BasePage


class MainPage(BasePage):

    # def __init__(self,driver):
    #     self.driver=driver
    addresslist_element = (MobileBy.XPATH,"//*[@text='通讯录']")
    def goto_addresslist(self):
        # 进入首页后，点击下方'通讯录'
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)