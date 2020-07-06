#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

import pytest

from case.commom_function import update_info
from common.read_yaml import get_yaml_date

curpath = os.path.dirname(os.path.realpath(__file__))
# print(curpath)
yamlpath = os.path.join(curpath, "update_info.yaml")
# print(yamlpath)
testdatas= get_yaml_date(yamlpath)
# print(testdatas["test_info_params"])


@pytest.mark.skip("跳过原因：有bug")
def test_2():
    """已经知道这个接口有bug"""
    print("已经知道这个接口有bug")

# test_datas = [
#             ("F",{'message': 'update some data!', 'code': 0,}),
#             ("M",{'message': 'update some data!', 'code': 0,}),
#             ("X",{'message': '参数类型错误', 'code': 3333,}),
#             ]
#
@pytest.mark.parametrize("test_input, expected",
                         testdatas["test_info_params"],
                         ids=[
                             "修改个人信息sex=F,成功",
                             "修改个人信息sex=M,成功",
                             "修改个人信息sex=X,异常场景",
                         ])
def test_info_1(login_fixture, test_input, expected):
    """测试修改个人信息接口"""
    print("用例1")
    s = login_fixture
    # print(s.headers)
    # if not s.headers.get("Authorization", ""):
    #     pytest.skip("未登录成功。跳过后面用例")
    infos = update_info(s, sex=test_input)
    print(infos)
    assert infos["message"] == expected["message"]
    assert infos["code"] == expected["code"]

@pytest.mark.xxx
def test_3(login_fixture):
    print("121212121")
@pytest.mark.xxx
def test_4(login_fixture):
    print("xxxxx")

