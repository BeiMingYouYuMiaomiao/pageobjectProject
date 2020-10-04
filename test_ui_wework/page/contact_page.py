# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


from test_ui_wework.page.basepage import BasePage


class ContactPage(BasePage):

    def goto_addmember(self):
        from test_ui_wework.page.add_member import AddMember
        return  AddMember(self.driver)

    def get_memberlist(self):
       name_list = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
       names=[]
       for name in name_list:
           names.append(name.text)
       return names
    def get_phone_error_message(self):
       errormessage = self.driver.find_element(By.CSS_SELECTOR,'.ww_inputWithTips_WithErr .ww_inputWithTips_tips').text

       return errormessage