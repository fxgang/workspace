# -*- coding: utf-8 -*-
#定义图书类
class Book(object):
    """
    公共属性
    """
    btype=""

    """
    私有属性
    """
    _cpy=""
    _indexpage = 1

    """
    构造方法
    """
    def __init__(self, name, page, sall=20.9867):
        """
        描述:带有参数的构造函数
            __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
            __init__方法有参数时，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
        :param name:
        :param page:
        :return:
        """
        self.name = name
        self.page = page
        self.sall = sall
        self._user="user"
        self.__password="96811"
        print("BooK构造，创建一个实例：", self.__class__.__name__)
        print("Book构造。名字属性：", self.name)

    def printbook(self):
        """
        打印书名，页数
        :return:
        """
        print(f"BooK类-->书名：{self.name}，总计：{self.page}页", self.__class__.__name__)

    def getspec(self):
        """
        计算书本厚度
        :return:
        """
        if self.page <= 200:
            return "本书较薄"
        else:
            return "本书较厚"

    def setcpy(self, cpy):
        """
        设置出版社
        :return:
        """
        self._cpy = cpy

    def getcpy(self):
        """
        获取出版社
        :return:
        """
        return self._cpy

#region 使用类.基本
"""        
#使用图书类
book = Book("C#编程宝典", 120)
print(type(book))
print(book)
book.name = "Java编程思想"
print(book.name)

book1 = Book("C#从入门到精通", 680)
book1.printbook()
book.printbook()
print(book.getspec(), book1.getspec())
"""
#endregion

#region 使用类.动态绑定属性.属性访问限制.私有.公有
"""
book = Book("PHP内核编程", 538)
book1 = Book("Java编程思想", 286, 45)
rst = book.name + "：共计：" + str(book.page) + "，预售价：" + format(book.sall, ".2f")

#book增加动态属性 author
book.author="吴琼今"
rst += "，本书作者：" + book.author
print(rst)

#属性author仅在book中动态增加，所以book1没有author下面的代码会出错
rst = book1.name + "：共计：" + str(book1.page) + "，预售价：" + format(book1.sall, ".2f")
#rst += "，本书作者：" + book1.author
rst += "，本书作者：" + book1.btype
print(rst)

book.setcpy("重庆图书出版社")
print(book.getcpy())

#新增一个属性__password
book.__password="qaz@123"
print(book.__password)

#访问类中已经定义好的属性__password
print(book._Book__password)
"""
#endregion

#region 继承与多态
class TchBook(Book):
    #重载printbook方法
    def printbook(self):
        print(f"TchBooK类-->书名：{self.name}，总计：{self.page}页", self.__class__.__name__)

class PcBook(Book):
    def __init__(self, name):
        #若不设置 self.name 则PcBook中没有name属性，因为子类中有__init__ 而没有显示的调用父类__init__
        self.name ="电脑类图书：" + name
        #如果不设置page属性 则父类中printbook方法调用时会报错，page属性没有定义
        self.page = 0
        print("子类PcBook构造，创建一个实例：", self.__class__.__name__)
        print("子类PcBook构造，名字属性：", self.name)

    #重载printbook方法
    def printbook(self):
        print(f"PcBooK类-->书名：{self.name}，总计：{self.page}页", self.__class__.__name__)

class VodBook(Book):
    def __init__(self, name, page, sall):
        self.name=name
        self.page=page
        self.sall=sall
        super(VodBook, self).__init__(name, page, sall)
        self.name = "视频类图书：" + name
        print("子类VodBook构造，创建一个实例：", self.__class__.__name__)
        print("子类VodBook构造，名字属性：", self.name)

    #重载printbook方法
    def printbook(self):
        print(f"VodBooK类-->书名：{self.name}，总计：{self.page}页", self.__class__.__name__)
'''
#子类TchBook没有本身的__init__默认调用父类的__init__
tboo = TchBook("九年级数学", 349, 12.98)
#print(tboo.name)
tboo.printbook()

#子类PcBook本身定义了__init__父类的__init__不会被调用
pbook = PcBook("精品英语课程")
#print(pbook.name)
pbook.printbook()

#子类VodBook本身定义__init__同时在子类中显示调用了父类的__init__
vbook = VodBook("走遍中国", 1000, 450)
#print(vbook.name)
vbook.printbook()
'''
#region 多态测试.继承
'''
def showinfo(obf):
    """
    传入一个Book类对象，调用printbook方法
    :param obf:
    :return:
    """
    obf.printbook()
print("====================****====================")
lb=[Book("黄帝内经", 129), TchBook("九年级高中语文", 200, 24), PcBook("VC++从入门到精通"), VodBook("中国美食", 2000, 980.098)]
for b in lb:
    showinfo(b)
'''
#endregion

#region 多态测试
class Duck(object):
    def fly(self):
        print("鸭子沿着地面飞起来了")

class Swan(object):
    def fly(self):
        print("天鹅在空中翱翔")

class Plan(object):
    def fly(self):
        print("飞机轰隆隆的飞起来了")
'''
def fly(obj):
    """
    接受一个对象，该对象的模板类中定义了fly方法，而且fly方发的参数必须一致（*args, **kw）
    :param obj:
    :return:
    """
    obj.fly()

print("====================****====================")
lb=[Duck(), Swan(), Plan()]
for o in lb:
    fly(o)
'''
#endregion

#endregion

#region 使用type
"""
import advcodefunction
import functools
import types
tl=[]
tl.append(type(123))
tl.append(type("fxgang"))
tl.append(type(abs))
tl.append(type(advcodefunction.nowtime))
tl.append(None)
tl.append(type(123)==type(456))
tl.append(type(Book("",0,0)))
tl.append(type(VodBook("", 0, 0)))
tl.append(isinstance(Book("", 0, 0), PcBook)) #父类不是子类
tl.append(isinstance(PcBook("测试"), Book)) #由于是继承关系所以返回True 子类是父类
tl.append(type(lambda x: x*x)==types.LambdaType)
tl.append(type(123))
for t in tl:
    print(t)
print(dir(Book("", 0, 0)))

b = Book("开发测试平台的艺术", 200, 28.99)
tl=[]
tl.append(hasattr(b, "user"))
tl.append(hasattr(b, "name"))
tl.append(hasattr(b, "_cpy"))
setattr(b, "sall", 99.99)
tl.append(getattr(b, "sall", 45)) #存在sall返回sall的值99.99
tl.append(getattr(b, "price", 100)) #不存price时返回100
print(tl)
"""

#endregion

#region 类属性.实例属性
'''
class AddSum(object):
    #定义类属性
    score = 0.00

    def __init__(self):
        #定义实例属性
        self.name = ""
        self.age = 0
        self.score = 0.00

    def addvscore(self, cscore):
        self.score += cscore

    def addscore(self, cscore):
        AddSum.score += cscore

    @classmethod
    def addcscore(cls, cscore):
        #直接通过类名称使用类变量
        AddSum.score += cscore

    @staticmethod
    def addtscore(cscore):
        AddSum.score += cscore


#实例as1 as2方法addvscore增加实例变量score的值,两个实例变量各不相干
#类变量score仍然为0
as1 = AddSum()
as1.addvscore(10)
as1.addvscore(2)
print(as1.score, as1.__class__.score)

as2 = AddSum();
as2.addvscore(20)
as2.addvscore(8)
print(as2.score, as2.__class__.score)

#调用实例方法 addscore 增加类变量score的值
as1.addscore(5)
print(as1.__class__.score)

as2.addscore(10)
print(as2.__class__.score)

#直接通过类名调用类方法
AddSum.addcscore(20)
print("==>", as2.__class__.score)

#实例属性被删除后，则使用同名的类变量
print("删除实例属性score前：", as1.score, as1.__class__.score)
delattr(as1, "score")
as1.addvscore(8)
print("删除实例属性score后：", as1.score, as1.__class__.score)

#删除实例as1中的name实例属性后 print(as1.name) 会报错
#但是不影响实例as2
delattr(as1, "name")
print(">>>>", as2.name)
#print(as1.name)

#调用静态方法 可以通过类，实例调用
print("增加类score前：", as1.score, as1.__class__.score)
AddSum.addtscore(20)
print("类增加类score后：", as1.score, as1.__class__.score)
as1.addtscore(8)
print("实例增加类score后：", as1.score, as1.__class__.score)

#调用类方法
print("调用类方法前：", as1.score, as1.__class__.score)
AddSum.addcscore(8)
print("类名调用类方法后：", as1.score, as1.__class__.score)
as1.addcscore(9)
print("实例调用类方法后：", as1.score, as1.__class__.score)
as1.__class__.addcscore(10)
print("实例类调用类方法后：", as1.score, as1.__class__.score)

#删除类中的方法 addvscore 后实例中的addvscore方法也已经失效
del AddSum.addvscore
#as1.addvscore(12)


#动态绑定方法.类
def addvscore(self, x):
    self.score += (x*x)
AddSum.addvscore = addvscore

print("类增加类实例方法前：", as1.score, as1.__class__.score)
as1.addvscore(10)
print("类增加类实例方法后：", as1.score, as1.__class__.score)

#动态绑定方法.实例
del AddSum.addvscore
from types import MethodType
as1.addvscore = MethodType(addvscore, as1)
print("实例增加类实例方法前：", as1.score, as1.__class__.score)
as1.addvscore(2)
print("实例增加类实例方法后：", as1.score, as1.__class__.score)
#增加的方法只对as1有效 所以下面的语句是错误的
#as2.addvscore(2)
'''
#endregion

#region __slots__ @property

class Person(object):
    __slots__ = ("name", "age", "_mcode")
    def __init__(self, name, age, mcode = "10010"):
        self.name = name
        self.age = age
        self._mcode = mcode

    def info(self):
        print(f"你好：{self.name},现在:{self.age}岁了，检测到你的手机号码：{self._mcode}")

    def set_age(self,val):
        if not isinstance(val, int):
            raise ValueError("age必须是一个整数")
        if val<0:
            raise ValueError("age必须大于0")
        if val>200:
            raise ValueError("有这么大的年龄吗，请联系管理员")
        self.age = val

    def get_age(self):
        return self.age

    @property
    def pname(self):
        return self.name

    @pname.setter
    def pname(self, val):
        if (not isinstance(val, str)) or (str is None):
            raise ValueError("请输入正确的姓名")
        if len(val)<3 or len(val)>15:
            raise ValueError("情书正确的姓名长度")
        self.name = val

    @property
    def mcode(self):
        return self._mcode
'''
wj = Person("fxgang", 45)
wj.info()
#不能增加adr属性 因为__slots__限制
#wj.adr = "四川"
wj.set_age(100)
print(wj.get_age())
wj.pname = "张三丰"
#属性mcode是只读的 下面的语句将出现错误
#wj.mcode = "13990029080"
wj.info()
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''
#endregion