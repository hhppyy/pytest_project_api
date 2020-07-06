#!/user/bin/python
# -*- coding:utf-8 -*-


import pytest
import requests
from case.commom_function import login, update_info, get_info


@pytest.fixture(scope="session")
def login_fixture():
    """先登录"""
    print("\n输入账号密码先登录")
    s = requests.session()
    login(s)
    if not s.headers.get("Authorization",""):
        pytest.skip("跳过用例")
    yield s
    print("后置操作")
    s.close()


@pytest.fixture(scope="session")
def unlogin_fixture():
    """不登录"""
    print("不登录")
    s = requests.session()
    return s
