# -*- coding: utf-8 -*-
def myadd(x, y):
    """
    功能：计算俩个数之和,以供reduce调用
    :param x:
    :param y:
    :return:
    """
    return x + y

def mycp(x, y):
    """
    功能:组合数字
    :param x:
    :param y:
    :return:
    """
    return x*10 + y

def isoddigt(x):
    """
    功能：判断x是否为偶数
    :param x: 等待判断的数据
    :return: 偶数返回:True 奇数返回:False
    """
    if 108 == x:
        return False
    else:
        return  0 == x%2

def oddlist():
    """
    功能:奇数列表生成器
    :return:
    """
    n = 1
    while(True):
        n = n + 2
        yield n
    return "DONE"