# -*- coding: utf-8 -*-
def mytrim(s):
    """
    功能：去掉字符串中的空格
    :param s: 传入字符串
    :return: 返回去掉空格后的字符串
    """
    if (s is None) or (not isinstance(s, str)):
        raise Exception("输入正确的字符串")
    sp = ' '
    if (not sp in s):
        return sp
    rst = ""
    while(sp in s):
        i = s.index(sp)
        rst += s[:i]
        s = s[i + 1:len(s)]
    rst += s
    return rst

def fibonacci(n):
    """
    功能:计算到n的斐波拉契数列
    :param n:最大值
    :return:返回一个fibonacct列表
    """
    i,a,b=0,0,1
    lt=[]
    while(i<n):
        lt.append(b)
        a, b = b, a + b
        i = i + 1
    return lt

def fibgenerator(n):
    """
    功能：实现一个斐波那契数列的生成器
    如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
    :param n: 最大值
    :return: 返回完成标志 0
    """
    i, a, b = 0, 0, 1
    while(i < n):
        yield b
        a, b = b, a + b
        i = i + 1
    return  0

def flgenerator():
    """
    功能:定义一个流程演示器生成器
    :return: "DONE" 表示完成
    """
    rst = "1.检测安装环境"
    yield rst
    rst = "2.下载平台支持包：包括各种类库、图文资源"
    yield  rst
    rst = "3.开始安装"
    yield rst
    rst = "4.安装完成，填写注册信息，注册账号"
    yield rst
    rst = "5.开始游戏... ..."
    yield rst
    rst = "DONE"
    return  rst