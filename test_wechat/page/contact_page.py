# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from test_wechat.page.add_department_page import AddDepartment

from test_wechat.page.base_page import BasePage
from test_wechat.page.import_contact_page import ImportContact


class Contact(BasePage):
    def goto_addmember(self):
        from test_wechat.page.add_member_page import AddMember
        return AddMember(self.driver)

    def add_department(self):
        self.find(By.CSS_SELECTOR,'.member_colLeft_top_addBtn').click()
        self.find(By.CLASS_NAME,'js_create_party').click()
        self.find(By.CSS_SELECTOR,'.inputDlg_item .ww_inputText').send_keys('我是部门1')
        self.find(By.CSS_SELECTOR,'.js_parent_party_name').click()
        self.find(By.XPATH,'/html/body/div[4]/div/div[2]/div/form/div[3]/div/div/ul/li/a').click()
        self.find(By.CSS_SELECTOR,'[d_ck="submit"]').click()
        return Contact(self.driver)

    def get_department_name(self):
        departmentnames = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-anchor')
        depnames = []
        for name in departmentnames:
            depnames.append(name.text)
        return depnames


    def goto_importcontact(self):
        self.find(By.CSS_SELECTOR,'.ww_btn_PartDropdown_left').click()
        self.find(By.CSS_SELECTOR,'.qui_dropdownMenu_itemLink ww_dropdownMenu_itemLink js_import_member').click()
        return ImportContact(self.driver)

    def get_memberlist(self):
        name_list = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for name in name_list:
            names.append(name.text)
        print(names)
        return names