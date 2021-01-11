# -*- coding: utf-8 -*-
#region 高阶函数 map
#map()函数接收两个参数
#   一个是函数，一个是Iterable
#   map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
"""
from myabs import mypower
gl = map(mypower, range(1, 11))
rst = ""
for p in gl:
    rst += f"{p}\t"
print(gl)
print(rst)
# 通过for p in gl生成器已经完成了所有计算,此时list(gl)为空，所以要重新定义一下
gl = map(mypower, range(1, 11))
print(list(gl))

#仅仅用一行代码就可以把数字列表转换为字符串列表
lst = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(lst)
"""
#endregion

#region 高阶函数 reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
#   这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
"""
from functools import reduce
from advcodefunction import  myadd
hj = reduce(myadd, list(range(1, 101)))
print(f"计算结果：{hj}")

from advcodefunction import mycp
hj = reduce(mycp, [1,5,8,9,2])
print(f"计算结果：{hj}")
"""
#endregion

#region 高阶函数 filter
#和map()类似，filter()也接收一个函数和一个序列
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""
from advcodefunction import isoddigt
lt = list(range(99,199))
gl = filter(isoddigt, lt)
rst = ""
for g in gl:
    rst += f"{g}\t"
print(rst)

from advcodefunction import oddlist
"""
#endregion

#region 高阶函数
"""
#sorted()函数就可以对list进行排序
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
li=[36, 5, -12, 9, -21]
print("排序前：", li)
lis = sorted(li)
print("排序后：", lis)

li3=sorted(li, key=abs)
print("使用key=abs排序后：", li3)

li4=sorted(li, key=abs, reverse=True)
print("使用key=abs倒序排序后：", li4)

"""
#endregion

#region 函数作为返回值
"""
from advcodefunction import lazy_sum
lt = list(range(10, 21))
f = lazy_sum(*lt)
print(f())

from advcodefunction import count
f1, f2, f3 = count()
print(f1(), f2(), f3())

from advcodefunction import count1
f1 = count1()
print(f1)

from advcodefunction import count2
f1, f2, f3 = count2()
print(f1(), f2(), f3())

from advcodefunction import createlist
f = createlist()
print(f(),f(),f(),f(), f())

from advcodefunction import createlist1
f = createlist1()
print(f(),f(),f(),f(), f(), f())

from advcodefunction import createlist2
f = createlist2()
print(f(),f(),f(),f(), f(), f())
"""

#endregion

#region 匿名函数
"""
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
#f = lambda x, *args, para, **kwargs : [args, para, kwargs]
lt = list(map(lambda x: x*x, list(range(1, 21))))
print(lt)

f = lambda x: x*x
print(f(30))

from advcodefunction import addsum
f = addsum(10, 20)
print(type(f))
print(f(10, 20))
"""
#endregion

#region 装饰器 decorator
"""
from advcodefunction import nowtime
#由于nlog()是一个decorator，返回一个函数，
#所以，原来的nowtime()函数仍然存在，只是现在同名的f变量指向了新的函数，于是调用nowtime()将执行新函数，即在nlog()函数中返回的wrapper()函数。
#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
f = nowtime
#print(f.__name__, f.__doc__, f.__code__)
print(f(), f.__name__)

from advcodefunction import nowtime1
#首先执行@plog("冯小刚")，返回的是decorator函数，
#再调用返回的函数，参数是nowtime1函数，返回值最终是wrapper函数。
#以上两种decorator的定义都没有问题，但还差最后一步。因为函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'nowtime'变成了'wrapper'：
f = nowtime1
print("\n", f(), f.__name__)
"""
#endregion

#region 偏函数 Partial function
#f = functools.partial(参数1，参数2，参数3)
#参数1：函数对象，int
#参数2：*args  可变参数，接收tuple，list，'100110010'
#参数3：*kw  关键字参数，接收dict, { 'base': 2 }
import functools
f = functools.partial(int, base=2)
print(f('100110010'))
print(f('ff', base=16))
#endregion