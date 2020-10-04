# -*- coding: UTF-8 -*-
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin2():
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.debugger_address = 'localhost:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3000)

    def teardown_method(self, method):
        self.driver.quit()

    def test_context(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        #断言  //*[@id="menu_contacts"]/span

        myclass = self.driver.find_element(By.LINK_TEXT,"通讯录").get_attribute("class")
        # print(myclass)
        assert  "frame_nav_item frame_nav_item_Curr" == myclass

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = [{'domain': '.work.weixin.qq.com', 'expiry': 1604209153, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852037623064'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'K0Anztepm3yZ9AQuphDYkBb7di4PfObnJGEXI6SUfvU6eUd-KoIakfw_LEylnL8lw8knlDSG10xLzBuukK-UT3ImRnaBM1d8odtN9lvXLIOtxvbISgQswjsPFbiAI9Fb1U4tnD6aJ60i8eiVz6RCM3zU6KwJeJ7ZbNY0XnDmGOCmcJH9hBjC_EQ0llEdosMHjzNJvB2KL5bQv-UFo6pUAuWjzf_0DdKQXUpCxyQ67zEul7ehTrvX-V4zk7oH7StVRD91MXv8OHcrwhOZTX6T-Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852037623064'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324952169020'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HglKwTj5k-zt4UYOriyP2CvsecbvMiGLNsYIqquTWS_rYwldGm-_7QA0AU725I8V'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9682155'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1832026590761536'}, {'domain': 'work.weixin.qq.com', 'expiry': 1601645177, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5d3cae8'}, {'domain': '.qq.com', 'expiry': 1601703552, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1164940469.1601613649'}, {'domain': '.qq.com', 'expiry': 1664689152, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.677458190.1601613649'}, {'domain': '.work.weixin.qq.com', 'expiry': 1633149641, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1906718202, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_511741689'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1633150821, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1601613648,1601614821'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2692836300'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '247c0f8723aa3ab4b84b3061bd3263358c6e55438278f9848f862b35338c1825'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '511741689'}, {'domain': '.qq.com', 'expiry': 1601617212, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5679074304'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'iCC1GN13eW'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
    def test_shelve(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'expiry': 1604209153, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852037623064'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'K0Anztepm3yZ9AQuphDYkBb7di4PfObnJGEXI6SUfvU6eUd-KoIakfw_LEylnL8lw8knlDSG10xLzBuukK-UT3ImRnaBM1d8odtN9lvXLIOtxvbISgQswjsPFbiAI9Fb1U4tnD6aJ60i8eiVz6RCM3zU6KwJeJ7ZbNY0XnDmGOCmcJH9hBjC_EQ0llEdosMHjzNJvB2KL5bQv-UFo6pUAuWjzf_0DdKQXUpCxyQ67zEul7ehTrvX-V4zk7oH7StVRD91MXv8OHcrwhOZTX6T-Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852037623064'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324952169020'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'HglKwTj5k-zt4UYOriyP2CvsecbvMiGLNsYIqquTWS_rYwldGm-_7QA0AU725I8V'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a9682155'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1832026590761536'}, {'domain': 'work.weixin.qq.com', 'expiry': 1601645177, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5d3cae8'}, {'domain': '.qq.com', 'expiry': 1601703552, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1164940469.1601613649'}, {'domain': '.qq.com', 'expiry': 1664689152, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.677458190.1601613649'}, {'domain': '.work.weixin.qq.com', 'expiry': 1633149641, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1906718202, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_511741689'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1633150821, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1601613648,1601614821'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '2692836300'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '247c0f8723aa3ab4b84b3061bd3263358c6e55438278f9848f862b35338c1825'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '511741689'}, {'domain': '.qq.com', 'expiry': 1601617212, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5679074304'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'iCC1GN13eW'}]
        db = shelve.open("mydb/logincookies")
        db['cookie'] = cookies
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()

    def test_memberjoin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db = shelve.open("mydb/logincookies")
        cookies = db['cookie']
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)

        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        # self.driver.find_element(By.CLASS_NAME,'memberJoin_link js_importExcel').click()
        self.driver.find_element(By.CLASS_NAME,'ww_fileImporter_fileContainer_uploadInputMask').send_keys('/Users/yuxin/Documents/testfile/test.xlsx')

        assert 'test.xlsx' == self.driver.find_element(By.CLASS_NAME,'ww_fileImporter_fileContainer_fileNames').text