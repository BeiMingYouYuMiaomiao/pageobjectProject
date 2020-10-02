# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin():
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(3000)

    def teardown_method(self, method):
        self.driver.quit()

    def test_context(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        #断言  //*[@id="menu_contacts"]/span

        myclass = self.driver.find_element(By.LINK_TEXT,"通讯录").get_attribute("class")
        # print(myclass)
        assert  "frame_nav_item frame_nav_item_Curr" == myclass