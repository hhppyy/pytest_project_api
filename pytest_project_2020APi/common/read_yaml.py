#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import yaml


def get_yaml_date(yamlpath):
    """
    """
    f = open(yamlpath, "r", encoding="utf-8")
    yamldate = f.read()
    print(yamldate)#字符串

    #把yaml文件数据转成字典
    d = yaml.load(yamldate, Loader=yaml.FullLoader)#需加Loader参数
    f.close()
    return d

if __name__ == '__main__':
    curpath = os.path.dirname(os.path.realpath(__file__))
    print(curpath)
    yamlpath = os.path.join(curpath, "update_info.yaml")
    print(yamlpath)
    a = get_yaml_date(yamlpath)
    print(a)
