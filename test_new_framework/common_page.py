# -*- coding: UTF-8 -*-
from test_new_framework.basepage import BasePage


class CommonPage(BasePage):
    def __getattr__(self, item):
        self._method_name =item

        return self._po_method

    def _po_method(self,**kwargs):
        self.go_run(self._method_name,**kwargs)