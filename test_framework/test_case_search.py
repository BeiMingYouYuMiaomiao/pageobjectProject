# -*- coding: UTF-8 -*-
import pytest
import yaml

from test_framework.page_demo import PageDemo
from test_framework.utils import Utils


class TestCase:

    def setup_class(self):
        self.pagedemo = PageDemo()
        self.pagedemo.start()

    def teardown_class(self):
        self.pagedemo.stop()

    def setup(self):
        pass

    def teardown(self):
        self.pagedemo.go_run('back')

    data = Utils.data_from_yaml(path='test_search.yaml')
    @pytest.mark.parametrize(data['keys'],data['values'])
    def test_search(self,keywords):
        self.pagedemo.search(keywords)
