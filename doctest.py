# -*- coding: utf-8 -*-
def abs(n):
    """
    功能：获得n的绝对值
    示例：
    abs(1) == 1
    abs(-1) == 1
    abs(0) == 0
    :param n: 参数
    :return: 返回绝对值
    """
    return  n if n >= 0 else (-n)
