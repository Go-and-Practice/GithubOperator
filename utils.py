#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 2:42 下午
# @Author  : Johny Zheng
# @Site    : 
# @File    : utils.py
# @Software: PyCharm
# Running based on python3.6.2 environment


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError