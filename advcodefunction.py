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

def lazy_sum(*args):
    """
    功能:返回sum函数的lazy_sum函数
    :param args: 列表
    :return: 返回函数sum
    """
    def sum():
        ax=0
        for n in args:
            ax+=n
        return ax
    return sum

def count():
    """

    :return:返回一个列表，列表的元素是函数f
    """
    fs=[]
    #循环变量i在返回函数f中在不断增加，发生了变化，不满足闭包要求
    #可以参见count2
    for i in range(1, 4):
        def f():
            """

            :return:
            """
            return i*i
        #返回列表中的元素是函数
        fs.append(f)
    return fs

def count1():
    """

    :return:
    """
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        #返回列表中的元素是值
        fs.append(f())
    return fs

def count2():
    """

    :return:
    """
    def f(j):
        #返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
        #变量j在返回函数g中不会改变
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

def createlist():
    r = 0
    def counter():
        #nonlocal声明这个变量不是局部变量空间的变量，需要向上一个层级变量空间找这个变量
        nonlocal r
        r = r + 1
        return r
    return counter

def createlist1():
    r = [0]
    def counter():
        r[0] = r[0] + 1
        return r[0]
    return counter

def createlist2():
    #定义一个生成器函数
    def iterator():
        r = 0
        while(True):
            r = r +1
            yield r
    g = iterator()
    #内部函数调用生成器函数
    def counter():
        return next(g)
    return counter

def addsum(x, y):
    """
    功能:返回匿名函数
    :param x:
    :param y:
    :return: 返回函数
    """
    return lambda x, y:x*x + y*y

def nlog(f):
    """
    功能:实现一个装饰器
    :param f:
    :return:
    """
    def wrapper(*args, **kw):
        print("调用：%s():" % f.__name__)
        return f(*args, **kw)
    return wrapper

@nlog
def nowtime():
    """
    功能：返回系统当前时间
    :return:
    """
    import datetime
    rst = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return rst

def plog(txt):
    def decorator(f):
        #因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
        #不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的
        import functools
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print("%s %s()" % (txt, f.__name__))
            return f(*args, **kw)
        return wrapper
    return decorator

@plog("冯小刚")
def nowtime1():
    """
    功能：返回系统当前时间
    :return:
    """
    import datetime
    rst = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return rst


