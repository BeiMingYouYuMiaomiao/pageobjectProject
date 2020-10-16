# -*- coding: UTF-8 -*-
import pytest

from UI自动化测试框架.page.app import App


class TestMain:
    @pytest.mark.parametrize('a,b',)
    def test_main(self):
        app=App()
        app.main().goto_search()