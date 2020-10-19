# -*- coding: UTF-8 -*-
from test_new_framework.basepage import BasePage


class PageLogin(BasePage):
    def login_by_password(self,email,password):
        self.go_run('login_by_password',email=email,password=password)
