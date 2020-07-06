#!/usr/bin/python
# -*- coding:utf-8 -*-

import pytest
from case.commom_function import register
from common.connet_mysql import execute_sql


@pytest.fixture(scope="function")
def delete_register():
    """前置，执行sql，删除注册"""
    sql = "DELETE from UserInfo where username='test001';"
    execute_sql(sql)


def test_register_1(unlogin_fixture, delete_register):
    """测试用例：注册"""
    s = unlogin_fixture
    r = register(s)
    print(r.text)
    assert "恭喜您，账号已成功注册" in r.text
#
# def test_register_2(unlogin_fixture, delete_register):
#     """测试用例：重复注册"""
#     s = unlogin_fixture
#     r1 = register(s)
#     print(r1.text)
#     r2 = register(s)
#     print(r2.text)
#     assert "恭喜您，账号已成功注册" in r1.text
#     assert "该用户名已被注册，请更换用户名" in r2.text
