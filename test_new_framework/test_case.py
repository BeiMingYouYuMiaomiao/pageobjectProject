# -*- coding: UTF-8 -*-
import pytest
import yaml

from test_new_framework.basepage import BasePage
from test_new_framework.common_page import CommonPage
from test_new_framework.page_demo import PageDemo
from test_new_framework.page_login import PageLogin
from test_new_framework.utils import Utils


class TestCase:
    testcase_file='test_search.yaml'
    po_file='page_demo.yaml'
    data = Utils.data_from_yaml(testcase_file)

    # 对PO的改造就是接收一个po_file文件，利用传参来定义不同的PO，而不是用不同的class
    # 那么就改造basepage，让它支持参数
    def setup_class(self):
        self.app = BasePage()
        self.app.start()

        # self.pagedemo.start()

    def teardown_class(self):
        self.app.stop()

    def setup(self):
        pass

    def teardown(self):
        # self.pagedemo.go_run('back')
        pass

    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self,keywords):
        self.pagedemo.search(keywords)

    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common(self, keywords):
        commonpage = CommonPage(self.po_file)
        commonpage.search(keyword=keywords)
        commonpage.back()


    def test_login(self):
       po_file='page_login.yaml'
       login=PageLogin(po_file)
       login.login_by_password(email='511741689', password='123456')


    def test_common_login(self):
        po_file='page_login.yaml'
        login=CommonPage(po_file)

        login.login_by_password(email='511741689', password='123456')