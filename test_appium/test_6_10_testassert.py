# -*- coding: UTF-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestSeniorPosition:

    def test_hamcrest(self):
        # assert_that(10,equal_to(10))
        # 如果断言失败，可以加一个提示
        # assert_that(10,equal_to(9),"断言失败了的提示")
        # assert_that(7,close_to(10,3))
        assert_that("contains some string",contains_string("string"))

