#!/usr/bin/python
# -*- coding:utf-8 -*-

import pytest

#组合参数，期望结果只能是一个

@pytest.mark.parametrize("psw", ["", 123, "aaaa"])
@pytest.mark.parametrize("username", ["", 234, "aaaa"])
def test_eval(username, psw):
    print("\n账号和密码组合：%s，%s"%(username, psw))











