# -*- coding: utf-8 -*-

#导入myabs

#region 必选参数
"""
from myabs import myabs
print(myabs(9), myabs(-10))
print(myabs("op"))

from  myabs import myabs2
print(myabs2(-909), myabs2(-0.98))

from myabs import movepos
x,y = movepos(100, 100, 10, 0)
print("原来的坐标(100, 100)，移动后的坐标(%.2f,%.2f)"%(x, y))
print(f"原来的坐标(100, 100)，移动后的坐标({x},{y})")

from myabs import mypower
x = mypower(8)
print(x)

from myabs import mypower2
print(mypower2(3, 3))
#endregion
"""
#endregion

#region 默认参数

"""
from myabs import npower
x = npower(4)
y = npower(4, 3)
print(f"使用默认值调用结果：{x}，使用指数调用结果：{y}")

from myabs import  reginfo
rst = reginfo("fxgang", "fxg_ang@126.com")
print(rst)

#默认参数名称调用
rst = reginfo("chzwei", "fxgang@sina.com", id="510311197603062312")
print(rst)

rst = reginfo("jiangyaoqiao", "fxgang@qq.com", city="四川省内江市", id="5202111992051823124", age=28, mv="13990023269")
print(rst)

rst = reginfo("lizhqiang", "fxgang@qq.com", city="四川省内江市",  age=38, mv="13990023269")
print(rst)

from myabs import list_add
rst = list_add("fxgang")
print(rst)

#函数定义中的默认值设置lt=[]已经失效
rst = list_add("lzhqiang")
print(rst)

from myabs import  list_add2
rst = list_add2("fxgang")
print(rst)

#函数定义中的默认值设置lt=None不会失效
rst = list_add2("lzhqiang")
print(rst)
"""
#endregion

#region 传值传址
#传值的参数类型：数字，字符串，元组（immutable）
#传址的参数类型：列表，字典（mutable）
"""
from myabs import valaddr
#传值
mage = 10
#传址
mfav=["政经", "历史", "影视", "体育"]
#传址
mbk={"bh":1.68, "bw":71.5}
#传值
ms=(78.897, 80.908, 99.992, 68.09878)
print("调用前:", "age=", mage, "mfav=", mfav, "mbk=", mbk, "ms=", ms)
rst = valaddr("冯小刚", mfav, mbk, mage, ms)
print("调用结果：", rst)
print("调用后:", "age=", mage, "mfav=", mfav, "mbk=", mbk, "ms=", ms)
"""
#endregion

#region 可变参数

#region 常规方法
"""
from myabs import calc
d = list(range(1, 3))
print(d)
rst = calc(d)
print(rst)

e=(1, "test", '2', 3)
print(e)
rst=calc(e)
print(rst)

d=set(range(5))
print(d, "增加元素前：%d" % calc(d))
d.add("chain")
d.add(10)
print(d, "增加元素后：%d" % calc(d))
"""
#endregion

#region 可变参数
"""
from myabs import calc2
d=list(range(1, 3))
d.append("ok")
print(d)
print("(List)计算结果：", calc2(*d))

d=set(range(1, 3))
d.add(9)
print(d)
print("(Set)计算结果：", calc2(*d))

d=tuple(range(1, 3))
print(d)
print("(Set)计算结果：", calc2(*d))
"""
#endregion

#endregion

#region 关键字参数
"""
from myabs import keyinfo
rst = keyinfo("fxgang", 45)
print(rst)
dc={"身高":185, "体重":"75公斤", "血型":"AB"}
#字典dc在这里是传值调用，函数keyinfo不会修改dc的值
print("调用前：", dc)
rst = keyinfo("李志强", 28, **dc)
print("调用后：", dc)
print(rst)

rst = keyinfo("陈志伟", 24, 城市="四川-自贡", 邮编="643000", 体重=75, 身高="186厘米")
print(rst)

from myabs import keyinfo2
mname = "李志强"
mfav = ["地理", "军事", "财经", "体育", "象棋"]
rst = keyinfo2(mname, 34, *mfav, job = "神龙骑士", city = "中国四川省自贡市沿滩区仙市镇")
print(rst)
rst = keyinfo2(mname, 34, *mfav, job = "神龙骑士")
print(rst)

from myabs import keyinfo3
rst = keyinfo3(mname, 30, sex="男", ctiy="中国四川省自贡市沿滩区仙市镇", 身高="175厘米")
print(rst)

rst = keyinfo3(mname, 30, sex="男2", ctiy="中国四川省自贡市沿滩区仙市镇", **dc)
print(rst)
"""

#endregion

#region 递归函数
from myabs import fact
n = 27
d = fact(n)
print("%d的阶乘是：%d" % (n, d))

from  myabs import  fact2
d = fact2(n)
print("%d的阶乘是：%d" % (n, d))
#endregion

#TODO 明天学习 高级特征

