# -*- coding: utf-8 -*-

#region 多重继承

#动物类
class Animal(object):
    pass

#哺乳动物
class Mammal(Animal):
    pass

#鸟类
class Bird(Animal):
    pass

#狗
class Dog(Mammal):
    pass

#蝙蝠
class Bat(Mammal):
    pass

#鹦鹉
class Parrot(Bird):
    pass

#鸵鸟
class Ostrich(Bird):
    pass

"""
Animal----Mammal----Dog
     |         |
     |         |----Bat
     |
     |----Bird----Parrot
             |
             |----Ostrich            
"""

#爬行
class Runnable(object):
    def run(self):
        print(self.__class__.__name__, "开始爬行... ...")

#飞行
class Flyable(object):
    def fly(self):
        print("开始飞行... ...")

#需要爬行的哺乳动物
#多重继承Mammal和Runnable类
class Cat(Mammal, Runnable):
    pass

"""
lcat = Cat()
lcat.run()
"""

#endregion

#region 混入 MixIn

#爬行类混入
class RunnableMixIn(object):
    def run(self):
        print(self.__class__.__name__, "开始爬行... ...")

#飞行类混入
class FlyableMixIn(object):
    def fly(self):
        print("开始飞行... ...")

#肉食类混入
class CarnivorousMixIn(object):
    def eatmeat(self):
        print(self.__class__.__name__, "开始吃肉了... ...")

    def run(self):
        print("肉食类动物的run... ...")

#混入肉食、爬行行为的哺乳动物
class Dogs(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
"""
dogs = Dogs()
dogs.run()
dogs.eatmeat()
"""
#endregion

#region 定制类
'''
class Student(object):
    def __init__(self, name):
        self.name = name
        #以下初始化两个数据供iter使用
        self.age = 10
        self.wgt = 17.5
    def __str__(self):
        return f"Student object (name：{self.name})"

    #__str__ 客服看到的结果
    #__repr__ 开发人员看到的结果 为调试所用
    __repr__ = __str__

    #实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self

    def __next__(self):
        #计算下一个
        #self.age = self.wgt
        #self.wgt = self.wgt + self.age
        self.age, self.wgt = self.wgt, self.age + self.wgt
        #返回值大于200抛出错误，退出计算
        if self.age > 200:
            raise StopIteration()
        return self.age

    #实现索引、切片、字典
    def __getitem__(self, n):
        #整数
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, b + a
            return a
        #切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            rl = []
            for x in range(stop):
                if x >= start:
                    rl.append(a)
                a, b = b, b +a
            return  rl

        #字典关键字
        if isinstance(n, str):
            dt = {"name":self.name, "age":self.age, "wgt":self.wgt}
            return dt.get(n)

    #设置属性
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getattr__(self, item):
        if item == "body":
            return f"身高：{self.wgt}"
        if item == "test":
            return 1024
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)
p = Student("张国伟")
print(p)
for age in p:
    print(age)
print(p[10])
print(p[1:10])
print(p["name"])
p["name"] = "蒋建平"
print(p["name"])
#这个属性在类中没有定义，但是类的__getattr__方法中处理了body
print(p.body)
#这个属性在类中没有定义，但是类的__getattr__方法中处理了test
print(p.test)
#这个属性在类中没有定义，但是类的__getattr__方法中也没有处理xyz 返回None
#raise AttributeError
#print(p.xyz)
'''
#endregion

#region 链式调用
'''
class Chain(object):
    #构造方法定义私有属性_path
    def __init__(self, path = ""):
        self._path = path
        self.name = "链式类"

    #返回类本身链式对象
    #在访问对象的item属性的时候，如果对象并没有这个相应的属性，方法，那么将会调用这个方法来处理。。。这里要注意的时，假如一个对象叫fjs,  他有一个属性：fjs.name = "fjs"，那么在访问fjs.name的时候因为当前对象有这个属性，那么将不会调用__getattr__()方法，而是直接返回了拥有的name属性了
    def __getattr__(self, item):
        return Chain(f"{self._path}/{item}")

    #返回类路径.实现响应客户的打印
    def __str__(self):
        return self._path

    __repr__ = __str__

    #实例调用时直接调用
    #__call__实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
    #你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
    def __call__(self, *args, **kw):
        #print()
        #print(f"调用前：{self._path}，调用参数：{path}")
        return Chain(f"{self._path}/{args[0]}")

    def say(self):
        print(f"告诉：{self._path} API调用完成")
#api = China() 实例化
#Chain().user 由于没有user属性，开始调用__getattr__ 从而有：Chain().users = Chain("/users") 至此这是重建Chain实例
#Chain().user("fxgang")
#Chain().user('fxgang') = Chain('/user')('fxgang') 这是对实例直接调用__call__，相当于调用普通函数一样
#关键步骤，这一步返回的是Chain('/users/fxgang'),再一次重建实例，覆盖掉Chain('/user'),
api = Chain().user("fxgang").timeline.list.dt
print(api, callable(api))
api.__call__("张建军")
api.say()

#region 判断属性还是方法
if hasattr(api, "name"):
    print("Chain中有属性name")
    if hasattr(api.name, "__call__"):
        print("name是方法")
    else:
        print("name是属性")
if hasattr(api, "say"):
    print("Chain中有属性say")
    if hasattr(api.say, "__call__"):
        print("say是方法")
    else:
        print("say是属性")

#endregion
'''

#endregion

#region 枚举
from enum import Enum
MOTH = Enum("Month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for n, v in MOTH.__members__.items():
    print(n, '==>', v, ',', v.value)
#endregion

#region 元类
#为元类创建的类准备方法
def fn(self, name="Wordl!"):
    print("Hello, %s" % name)
#1.class的名称；
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
Hello = type("Hello", (object,), dict(hello=fn))
h = Hello()
print(type(Hello), type(h))
h.hello()

"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
"""
class ListMetacclass(type):
    #1.当前准备创建的类的对象；
    #2.类的名字；
    #3.类继承的父类集合；
    #4.类的方法集合。
    def __new__(cls, name, bases, attrs):
        attrs["add"] = lambda self, value:self.append(value)
        return type.__new__(cls, name, bases, attrs)
    
class mlist(list, metaclass=ListMetacclass):
    pass
#标准的list类没有add方法，通过ListMetacclass元类创建的list具备add
lt = mlist()
lt.append("test")
lt.add(12)
'''
for i in lt:
    print(i)
'''    
#endregion

#region 元类设计ORM
class Field(object):
    def __init__(self, name, ctype):
        #字段名称
        self.name = name
        #字段类型
        self.ctype = ctype
        
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=="Model":
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" %name)
        mappings=dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping：%s==>%s" % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs["__mappings__"] = mappings
        attrs["__table__"] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __inti__(self, **kw):
        super(Model, self).__inti__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fs = []
        ps = []
        gs = []
        print("save--->",self.__mappings__.items())
        for k, v in self.__mappings__.items():
            fs.append(v.name)
            ps.append('?')
            gs.append(getattr(self, k, None))
        sql = "insert into %s (%s) values(%s)" % (self.__table__, ','.join(fs), ','.join(ps))
        print("SQL:%s" % sql)
        print("ARGS: %s" % str(gs))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name = "冯小刚", email="fxg_ang@126.com", password="fxg8")
u.save()
#endregion
