#! /usr/bin/python3
# -*- coding:utf-8 -*-
#region try except finally
import logging
def mdiv(a, b):
    r = 0
    try:
        r = a / b
    except ZeroDivisionError as ex:
        print("错误，除数不能为0", ex)
    except ValueError as ex:
        print("参数错误，只能是数字", ex)
    except TypeError as ex:
        logging.exception(ex)
        print("类型错误，只能是数字", ex)
    finally:
        print("运算完毕！")
    return r

#print(mdiv(10, 3), mdiv(9, 0), mdiv("ab", 3))
#endregion

#debug assert

def foo(s):
    n = int(s)
    import logging
    logging.basicConfig(level=logging.info())
    logging.info("n = %d" % n)
    assert n!= 0, "参数为0"
    return  10 / n

print(foo(10/3), foo('0'))

#endregion