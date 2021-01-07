# -*- coding: utf-8 -*-
# 开始Python之旅
# 输出运算符
#region 基本输入
'''
print("100+200=", 100+200)
name = input("输入你的姓名：")
print("好的，", name, "请稍等片刻");
age = input("请输入你的年龄：")
sex = input("请输入的性别：")
rst = ""
if int(age)>70:
    if (sex == "男"):
        rst = "大爷，你好"
    else:
        rst = "奶奶，你好"
else:
    if (sex == "男"):
        rst = "小伙子，好呀！"
    else:
        rst = "姑娘，年轻真好！"
print(rst)
'''
#endregion

#region 输出格式
"""
# 分别输出16进制 浮点数 8进制 2进制 hex oct bin
print(0x10,1.23-5,0o10,0b100, bin(9999), format(9999,"b"))

# r原样输出
rst = r"这个一个字符串，不要做任何转换:\\ \n远洋输入 \f"
print(rst)
rst = '''这是一个多行测试
...可以好好\n看看
...数据中心
...测试结果'''
print(rst)
rst = r'''这是一个多行测试
...可以好好\n看看
...数据中心
...测试结果'''
print(rst)
"""
#endregion

#region 基础输出
'''
rst = 100/3
print("一般除法：", rst)
rst = 100//3
print("结果证书：", rst)
rst = 100%3
print("结果余数", rst)

# 测试ord() chr()
print(ord("A"))
print((chr(98)))

#字符编码
rst = "这是一个中文测试,ok"
print("Abc".encode("ascii"))
print(rst,"长度=",len(rst))
rst = rst.encode("utf-8")
print(rst,"长度=",len(rst))
rst = rst.decode()
print(rst, ord('大'), hex(ord('大')), bin(ord('大')))
'''
#endregion

#region 格式输出
'''
PI=3.1415926
print(r'”原文：整数站位：%2d-前导站位：%02d%%%d--浮点站位：%.2f“ % (391, 1, 100, PI)', "\n==>>>格式化结果：整数站位：%2d-前导站位：%02d%%%d--浮点站位：%.2f" % (391, 1, 100, PI))
rst = "Hello, {0}, 成绩提升了 {1:.1f}%"
name = input("输入他的姓名：")
score = input("输入他的成绩：")
print("原文：", rst, "\n==>>>格式化结果：", rst.format(name, float(score)))
name = input("输入你的姓名：")
age = input("输入你的年龄：")
weight = input("输入你的体重：")
weight = float(weight)
rst = f"你好：{name}, 今年你{age}岁了，你的体重是：{weight:.2f}"
print(rst)
'''
#endregion

#region 复杂数据类型

#TODO 復雜類型.列表
'''
#  list []创建
gods=["显示器", "主机板", "CPU", "内存", "硬盘", "显示卡", "网络卡", "键盘", "鼠标", "显示卡", "声卡", "音响"]
rst = "总计配件：%d个" % len(gods), "其中第一个配件是：%s" % gods[0], "最后一个配件是：%s" % gods[-1]
print(gods, rst)

gods.append("游戏杆")
rst = "总计配件：%d个" % len(gods), "其中第一个配件是：%s" % gods[0], "最后一个配件是：%s" % gods[-1]
print(gods, rst)

gods.insert(0, "Windows OS 10")
rst = "总计配件：%d个" % len(gods), "其中第一个配件是：%s" % gods[0], "最后一个配件是：%s" % gods[-1]
print(gods, rst)
index = gods.index("显示卡")
gods.insert(index, "VS2019")
print(gods, rst)

index = gods.index("显示卡", index + 2, len(gods) - 1)
gods.insert(index, "Office2020")
rst = "总计配件：%d个" % len(gods), "其中第一个配件是：%s" % gods[0], "最后一个配件是：%s" % gods[-1]
print(gods, rst)

soft = ["Windows 10", "Ubuntu", "Os X 10.8"]
dev=["Vs2019", "Ecplipse", "Geidt"]
index = gods.index("VS2019")
gods[index] = dev
index = gods.index("Office2020")
gods[index] = soft
rst = "总计配件：%d个" % len(gods), "其中第一个配件是：%s" % gods[0], "最后一个配件是：%s" % gods[-1], "操作系统列表：", gods[index], "总共可以预装：%d个操作系统" % len(gods[index])
print(gods[index][0])
print(gods, rst)
'''

#TODO 復雜類型.元祖
'''
# tuple （）
mp = ("顯示屏", "CPU", "內存", "網絡", "服務商", "網速", "生產商")
print(mp, mp[0])
pds = ["北京", "上海", "天津", "重庆"]
pdf = ["辽宁", "吉林", "河北", "河南", "山西", "陕西", "山东", "四川", "湖北", "湖南"]
mp=("中国", pds, pdf, "日本", "新加坡", "泰国", "越南", "菲律宾", "文莱", "柬埔寨", "韩国", "朝鲜", "阿富汗")
print(mp, "中国有：%d个国家"%len(mp))
mp[1][0] = "广东"
print(mp, "中国有：%d个国家"%len(mp))
# 定义整形变量
age = (70)

# 定义元祖
ages = (70,)
print(age + 1)
print(ages[0] + 1)

#使用循环
for ct in mp:
    # print(ct, "类型是：", type(ct), "-->", isinstance(ct, list))
    if isinstance(ct, list):
        for ct2 in ct:
            print("国家：%s--->%s" % (ct, ct2))
    else:
        print("只有国家名称:%s" % ct)

digt = range(101)
digts = list(digt)
digtt = tuple(digt)
print("类型：", type(digt), type(digts), type(digtt))
sums = 0
for x in digt:
    sums+=x
    print("当前累计：", sums)
print("\n计算结果：", sums)
digts[1]=1010

#定义字典
# dict {}
china = {"直辖市":["重亲", "天津", "上海", "北京"], "行政特区":["香港", "澳门"], "省份":{"东北":["黑龙江", "辽宁", "吉林"], "西南":["四川", "云南", "贵州"], "华南":["广东", "广西", "福建"]}}
print(china)
print("特区：")
for tq in list(china["行政特区"]):
    print("特区：", tq)
for dq in list(dict(china["省份"])["西南"]):
    print("中国西南地区:", dq)
print("直辖市在china中所以结果为：", "直辖市" in china)
print("特区不在在china中所以结果为：", "特区" in china)
#定义集合
# set(list)
s1 = set(list(range(10)))
s1.add(1900)
print(s1)
s2 = set(list(range(5,20)))
print(s2)
print("s1,s2交集：", s1 & s2)
print("s1,s2合集：", s1 | s2)
s3 = set(s1.union(s2))
s3.add(1200)
print("s1,s2union操作：", s3)

#字符串的不可修改
stra="中国china"
print("修改前：", stra)
#此处调用replace修改
print(stra.replace("h", "l"))
#由于字符串不可以修改，所以stra没有变化
print("直接修改：", stra)
#此处修改stra的值,并将stra指向新的修改后的字符串对象
stra=stra.replace("c", "s")
print("修改后：%s" % stra)
'''

#endregion
