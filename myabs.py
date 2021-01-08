# -*- coding: utf-8 -*-
#导入数学函数库
import math
def myabs(num):
    """
    函数功能：计算num的绝对值
    :param num:数字(int, float)
    :return:正数或者0或者None
    """
    if (not isinstance(num,int)) and (not isinstance(num, float)):
        return None
    if num>0:
        return  num
    else:
        return -num

def myabs2(num):
    """
    函数功能：计算num的绝对值
    :param num: 数字，正数或者浮点数
    :return: 非负数
    """
    if not isinstance(num, (int, float)):
        raise TypeError("num参数类型错误，只能是正数或者浮点数")
    if num>0:
        return num
    else:
        return -num

def movepos(x, y, step, angle=0):
    """
    函数功能:移动点，从当前坐标，引动到新的坐标
    :param x:横坐标
    :param y:纵坐标
    :param step:步长
    :param angle:偏移角度,默认不偏移
    :return:返回新坐标的元组(nx, ny)
    """
    if not isinstance(x, (int,float)):
        raise TypeError("x必须是整数或者浮点数")
    if not isinstance(y, (int,float)):
        raise TypeError("y必须是整数或者浮点数")
    if not isinstance(step, (int,float)):
        raise TypeError("step必须是整数或者浮点数")
    if not isinstance(angle, (int,float)):
        raise TypeError("angle必须是整数或者浮点数")
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def mypower(x):
    """
    功能:计算x的平方
    :param x: 数字包括整数、浮点数
    :return: 返回x的平方
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x必须是数字包括整数和浮点数")
    return x*x

def mypower2(x, n):
    """
    功能:计算x的n次方
    :param x: 计算基数
    :param n: 次方数
    :return: 返回x的n次方
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x必须是数字包括整数和浮点数")
    if not isinstance(n, int):
        raise TypeError("n必须是整数")
    if n < 0:
        raise Exception("n必须大于等于0")
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 使用默认参数
def npower(x, n=2):
    """
    设置默认参数时，有几点要注意：
    1.必选参数在前，默认参数在后，否则Python的解释器会报错
    2.如何设置默认参数
    3.函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
    4.默认参数的值应该是不变对象str、None
    功能：计算x的n次方
    :param x: 次方计算中的基数
    :param n: 次方计算中的指数,默认为2计算平方
    :return: 返回x的你吃饭
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x必须是数字包括整数和浮点数")
    if not isinstance(n, int):
        raise TypeError("n必须是整数")
    if n < 0:
        raise Exception("n必须大于等于0")
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def reginfo(name, email, mv="13000000000", age=30, city="自贡", id="510311197508152371"):
    """
    功能:返回注册信息串
    :param name: 注册人姓名
    :param email: 注册人邮箱
    :param mv: 注册人手机号码
    :param age: 注册人年龄
    :param city: 注册人城市
    :param id: 注册人身份证号码
    :return: 注册人信息串
    """
    if not isinstance(age, int):
        raise TypeError("请输入正确的年龄数据")
    mvr="1\d{10}"
    import re
    if not re.match(mvr, mv):
        raise Exception("请输入正确的手机号码")
    emailr="\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*"
    if not re.match(emailr, email):
        raise Exception("请输入正确的邮箱地址")
    if not isinstance(name, str):
        raise TypeError("请输入正确的姓名")
    rst = '''欢迎：%s来到新软世界，
    正当：%d的你已经在：%s使用手机%s注册的新的世界账号，
    并留下的身份证号码:%s作为安全特征码。
    同时你也可以使用邮箱：%s登录我们的世界。
    \nOK再次欢迎你来到新软世界，我们的朋友：%s''' % (name, age, city, mv, id, email, name)
    return rst

def list_add(val, lt=[]):
    """
    功能：向列表中增加一个值
    :param val: 等待增加的值
    :param list: 等待增加值的列表，默认为空，多次采用默认参数调用是=[]会失效
    :return: 返回增加值这个列表
    """
    lt.append(val);
    return lt

def list_add2(val, lt=None):
    """
    功能：向列表中增加一个值
    :param val: 等待增加的值
    :param list: 等待增加值的列表，默认为None，多次采用默认参数调用是=None不会失效
    :return: 返回增加值这个列表
    """
    if lt is None:
        lt = []
    lt.append(val);
    return lt

def valaddr(name, fav, bk, age, scor):
    """
    功能：登记学员信息
    :param name: 学员姓名
    :param fav: 学员爱好列表
    :param bk: 学员身体特征字典
    :param age: 学员年龄
    :param scor: 学科成绩元组
    :return: 返回学员情况
    """
    rst = f"你好，{name}：同学 "

    #更改列表的值
    fav.append("军事")
    rst = rst + "\t你登记的爱好有："
    for x in fav:
        rst = rst + x + '\t'

    for k in bk:
        rst = rst + "\t你的%s是%s" % (k, bk[k]) + '\t'
    #更高字典的值
    bk["xm"] = "AB"

    rst = rst + "你的年龄是：%03d" % age
    #改变age的值
    age = 98

    rst = rst + "\t你的成绩分："
    for s in scor:
        rst = rst + str(format(s, ".2f")) + '\t'
    return rst


def calc(nums):
    """
    功能:计算列表、元组、集合元素平方跟和
    :param nums: 列表、元组、集合
    :return: 返回值
    """
    if not isinstance(nums, (set, tuple, list)):
        raise TypeError("参数类型错误")
    s=0
    for x in nums:
        if isinstance(x, (int, float)):
            s = s + mypower2(x, 2)
    return s

def calc2(*nums):
    """
    功能:计算列表、元组、集合平方和
    :param nums: 列表、元组、集合指针
    :return: 返回计算结果
    """
    if not isinstance(nums, (set, list, tuple)):
        raise TypeError("参数类型错误，只支持：列表、元组、集合")
    s=0
    for x in nums:
        if isinstance(x, (int, float)):
            s = s + mypower2(x, 2)
    return s

def keyinfo(name, age, **kw):
    """
    功能:计算会员信息
    :param name: 会员名称
    :param age: 会员年龄
    :param kw: 会员身体特征 dict
    :return: 返回会晕信息
    """
    rst = f"你好:{name}，欢迎{age}岁的你\n"
    if (not (kw is None)) and (len(kw)>0):
        rst += "你的体检报告如下：\n"
        for k in kw:
            rst += k + '：' + str(kw[k]) + "\t"
        kw["total"] = 2000
    print("函数中：", kw)
    return rst

def keyinfo2(name, age = 20, *tz, city = "四川.自贡.沿滩", job):
    """
    功能:注册信息，测试必选参数,默认参数,可变参数,关键字参数,关键字命名参数
        函数定义中已经有了一个可变参数(tz)，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
        命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
    :param name:注册名称
    :param age:注册年龄 带有默认值，如果不传递则采用tz（dict）中的第一个元素
    :param tz:注册者爱好dic
    :param city:注册者地址，命名关键字参数，具有默认值
    :param job:注册者职业，命名关键字参数，没有默认值
    :return:
    """
    rst = f"{age}的{name},欢迎来到新软世界"
    if (not (tz is None)) and (len(tz)>0):
        rst += "\t阁下的爱好有："
        for f in tz:
            rst += f + '\t'
    rst +="\n你出生的城市：" + city
    rst +="\t你的职业：" + job
    return rst

def keyinfo3(name, age = 20, *, ctiy = "四川.内江市", job = "黑龙骑士", sex, **att):
    """
    功能：组合注册会员信息
    在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
    这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

    对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
    :param name: 注册会员姓名
    :param age: 注册会员年龄，默认值20
    :param ctiy: 注册城市，命名关键字参数，有默认值
    :param job: 注册职业，命名关键字，有默认值
    :param sex: 注册性别，命名关键字
    :param att: 注册者附加信息，关键字参数(dict)
    :return:返回注册者综合信息
    """
    rst = f"{age}的{name}欢迎来到新软世界\t"
    rst += "\n\t你出生的地址：%s" % (ctiy)
    rst += "\n\t你选择的职业：%s" % (job)
    if sex == "男":
        rst += "\n我的先生，在世界你要努力哈"
    elif sex == "女":
        rst += "\n%s:小姐，努力吧，新软世界恭候已久" % (name)
    else:
        rst += "\n阁下，我该如何称呼你"
    if  (not (att is None)) and (len(att) > 0):
        rst += "\n你的其他信息如下："
        for k in att:
            rst += k + ":" + str(att[k]) + "\t"
    return  rst
