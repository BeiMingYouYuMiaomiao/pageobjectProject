# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By

from test_wechat.page.base_page import BasePage


class ImportContact(BasePage):
    def import_contact(self):
        self.find(By.CLASS_NAME,'ww_fileImporter_fileContainer_uploadInputMask').send_keys('/Users/yuxin/Documents/testfile/test.xlsx')
    def get_text(self):
        text = self.find(By.CLASS_NAME, 'ww_fileImporter_fileContainer_fileNames').text
        return text