# -*- coding: utf-8 -*-
"这是一个测试模块"

__author__ = "fxgang"

import sys

def test():
    """
    模块测试
    :return:
    """
    rst = ""
    args = sys.argv
    if len(args) == 1:
        rst = "你好，欢迎来到新软的世界!"
    elif len(args) == 2:
        name = args[1]
        rst = f"你好：{name}，欢迎来到新软的世界！"
    else:
        rst = "无效的运行参数，或者参数太多，例如：test [‘fxgang’]"
    print(rst)

def _getusername1(name):
    """
    内部函数：在本模块外部不应该被调用
    :param name:
    :return:
    """
    return f"你好：{name}"
def _getusername2(name):
    """
    内部函数：在本模块外部不应该调用
    :param name:
    :return:
    """
    return f"你好：{name}，你的名字太长了！"
def getusername(name):
    """
    公共函数：在本模块外部可以调用
    :param name:
    :return:
    """
    if len(name)>5:
        return _getusername2(name)
    else:
        return _getusername1(name)

if __name__ == "__main__":
    test()


