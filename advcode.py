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

#region 高阶函数 sorted
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

#endregion