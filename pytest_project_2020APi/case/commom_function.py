#!/usr/bin/python
# -*- coding:utf-8 -*-


import requests



def login(s, username="test", password="123456"):
    """
    登陆
    :param s: requests.session()
    :param username:账号
    :param password: 密码
    :return: s
    """
    url = "http://49.235.92.12:6009/api/v1/login"
    body = {
        "username": username,
        "password": password
    }
    r = s.post(url, json=body)

    token = r.json()["token"]
    # print(token) #获取到token

    h = {
        "Content-Type": "application/json",
        "Authorization": "Token %s" % token
    }
    s.headers.update(h)
    return s


def update_info(s, name="test", mail="123@qq.com", sex="M"):
    url = "http://49.235.92.12:6009/api/v1/userinfo"

    body = {
        "name": name,
        "sex": sex,
        "age": 23,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r.json()


def get_info(s):
    url = "http://49.235.92.12:6009/api/v1/userinfo"
    r = s.get(url)
    return r.json()


def register(s, username="test001", psw="123456", email="12353@qq.com"):
    # s = requests.session()
    url = "http://123.56.231.107:8000/api/register/"

    body = {
        "account": username,
        "email": email,
        "password": psw,
        "repassword": psw
    }

    h = {
        "X-Requested-With": "XMLHttpRequest"
    }

    r = s.post(url, json=body, headers=h)
    # print(r.text)
    # print(r.content.decode(encoding="utf-8"))
    return r


if __name__ == '__main__':
    s = requests.session()
    # login(s)  # 调用登陆函数
    # infos = update_info(s, name="test1", mail="123@qq.com")  # z调用修改个人信息函数
    # print(infos)
    # m = get_info(s)
    # print(m)
    register(s)
