# -*- coding: utf-8 -*-
#region 切片 slice
"""
fav = ["体育", "财经", "军事", "历史", "社会", "彩票", "影视", "话题", "生活"]
print(fav)
#去掉前面2个
fav1 = fav[2:len(fav)]
print(fav1)
#去掉最后2个
fav2 = fav[:len(fav)-2]
print(fav2)
#倒数3个到倒数1个之间
fav3 = fav[-3:-1]
print(fav3)
#最后4个
fav4 = fav[-4:]
print(fav4)
#复制
fav5 = fav[::]
print(fav5)

t = " fxg an g 123 fxgang use      r ok tes us     er ceo   si9 1289"
from advfunction import mytrim
ts = mytrim(t)
print(t)
print(ts)
"""
#endregion

#region 迭代 Iteration
"""
fav = ["体育", "财经", "军事", "历史", "社会", "彩票", "影视", "话题", "生活"]
rst = ""
for f in fav:
    rst += f + "\t"
print(rst)
bdt={"身高":168, "体重":"75公斤", "血型":"AB", "血糖":6.896, "血压":60, "电话":"13990023269", "addr":"四川省自贡市沿滩区仙市镇"}
print(bdt)

rst=""
for k in bdt:
    rst += "%s:%s\t" % (k, str(bdt[k]))
print(rst)

rst = ""
for k in bdt:
    rst += f"{k}\t"
print(rst)

rst = ""
for v in bdt.values():
    rst += f"{v}\t"
print(rst)

rst = ""
for k,v in bdt.items():
    rst += f"{k}:{v}\t"
print(rst)

#对象迭代判断
from collections.abc import Iterable
itr = isinstance(3, Iterable)
print(itr)
itr = isinstance("abcd", Iterable)
print(itr)
itr = isinstance(bdt, Iterable)
print(itr)

#list转换为枚举
rst = ""
bdten=enumerate(bdt)
for i, v in bdten:
    rst += f"第{i}个元素-->{v}\t"
print(rst)

rst = ""
lt=[(12,45), (16,48), (12,45), (13,46), (14,47), (12,45)]
for x, y in lt:
    rst += f"x={x} y={y}\t\t"
print(rst)
"""
#endregion

#region 列表生成式

#普通生成 列表
"""
from myabs import mypower
lt=[]
for x in range(1, 11):
    lt.append(mypower(x))
print(lt)

#列表生成式
lt = [mypower(x) for x in range(1, 11)]
print(lt)

#列表生成式.筛选
#for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
lt = [x * x for x in range(1, 11) if 0== x%2]
print(lt)
lt =[x if 0==x%2 else 0 for x in range(1, 11)]
print(lt)

#列表生成式.多层循环
lt =[f"{a}{i}" for a in "abcd" for i in "1234567890" if not a == 'c' or not i in '4,7']
print(lt)

import os
ds = [d for d in os.listdir("/home/fxgang/")]
print(ds)

#列表生成式从字典生成列表
ss={"语文":88, "数学":92, "英语":90, "法语":66, "政治":100, "体育":98, "物理":96, "化学":79, "地理":95, "历史":100}
lss = [f"{k}:{v}" for k,v in ss.items()]
print(lss)

#筛选字符串后变成小写
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L)
print(L2)
"""
#endregion

#region 生成器 generator
"""
#1.用()中使用列表生成式
#2.函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
g=(x*x for x in range(1,11))
print(g)
#print(next(g), next(g), next(g))
from collections.abc import Iterable
print(isinstance(g, Iterable))
rst = ""
for n in g:
    rst += f"{n}\t"
print(rst)

#调用函数生成斐波那契数列
from advfunction import fibonacci
lt = fibonacci(90)
print(lt)

#调用生成器来实现
from advfunction import  fibgenerator
g1 = fibgenerator(90)
rst = ""
for f in g1:
    rst += f"{f}\t"
print(rst)

#简单的流程生成器
from advfunction import  flgenerator
fl = flgenerator()
for fw in fl:
    print(fw)

fw = flgenerator()
while(True):
    try:
        print(next(fw))
    except StopIteration as ex:
        print("生成器返回最终值", ex.value)
        break
"""
#endregion

#region 迭代器 Iterable

#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function
#以上两类可以使用for循环来迭代数据
#可以使用isinstance()判断一个对象是否是Iterable对象

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterable
from collections.abc import Iterator
i1 = [x for x in range(1, 11)]
i2 = (x for x in range(1, 11))
print("i1-->isinstance(i1, Iterable) = ", isinstance(i1, Iterable), "isinstance(i1, Iterator)", isinstance(i1, Iterator))
print("i2-->isinstance(i2, Iterable) = ", isinstance(i2, Iterable), "isinstance(i2, Iterator)", isinstance(i2, Iterator))
#列表不是Iterator
#可以通过iter函数使Iterable变为Iterator
i3 = iter(i1)
print("i3-->isinstance(i3, Iterable) = ", isinstance(i3, Iterable), "isinstance(i3, Iterator)", isinstance(i3, Iterator))
print("i2-->isinstance(i2, Iterable) = ", isinstance(i2, Iterable), "isinstance(i2, Iterator)", isinstance(i2, Iterator))
while(True):
    try:
        print(next(i3))
    except StopIteration as ex:
        print("调用完成：", ex.value)
        break

#endregion