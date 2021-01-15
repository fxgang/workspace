# -*- coding: utf-8 -*-
"""
\d可以匹配一个数字
\w可以匹配一个字母或数字
\s可以匹配一个空格（也包括Tab等空白符）
.可以匹配任意字符
*表示任意个字符（包括0个）
+表示至少一个字符
?表示0个或1个字符
{n}表示n个字符
{n,m}表示n-m个字符
[]表示范围
A|B可以匹配A或B
^表示行的开头，^\d表示必须以数字开头
$表示行的结束，\d$表示必须以数字结束
match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。常见的判断方法就是
"""
import re
rs = "^\d{3}\-\d{3,5}$"
ss = "111-1234"
if re.match(rs, ss):
    print("搜索成功！")
else:
    print("搜索失败!")

#切分字符串
ds = "a, b   c, d "
ll = ds.split(' ')
print(ll)
ll = re.split(r"\s+", ds)
print(ll)
ll = re.split(r"[\s,]+", ds)
print(ll)

rs = r'^(\d{3})-(\d{3,8})$'
m = re.match(rs, "028-3804490")
print(m)

#贪婪匹配
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
ll = re.match(r'^(\d+)(0*)$', '102300').groups()
print(ll)

#必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
ll=re.match(r'^(\d+?)(0*)$', '102300').groups()
print(ll)

#编译正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
ll = re_telephone.match('010-12345').groups()
print(ll)
ll = re_telephone.match('010-8086').groups()
print(ll)