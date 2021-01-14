# -*- coding: utf-8 -*-

#region 读写txt文件
"""
def readfile(fname):
    rst = ""
    f = open(fname, 'r')
    try:
        rst = f.read()
    except IOError as ex:
        print(ex)
    finally:
        if f:
            f.close()
    return rst

fn = "/home/fxgang/doc/dayword.txt"
#fn = "/home/fxgang/doc/ubuntu.pdf"
#rst = readfile(fn)
#print(rst)

# with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的”清理”操作，释放资源，
# 比如文件使用后自动关闭、线程中锁的自动获取和释放等。
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
with open(fn) as sf:
    i=0
    for l in sf:
        i = i + 1
        print(i, '：', l)

fn = "/home/fxgang/doc/f001.txt"
with open(fn, 'w') as f:
    f.write("你好，这是写入的测试")
"""
#endregion

#region 读写内存
"""
from io import StringIO
f = StringIO()
f.write("我的数据")
f.write(' ')
f.write("需要安全保存")
print(f.getvalue())

f = StringIO(f.getvalue())
while(True):
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write("中文".encode("utf-8"))
print(f.getvalue())
"""
#endregion

#region 文件目录
#import os as myos
"""
snm = os.name
print(snm)
print(os.uname())
print(os.environ)
print(os.environ.get("PATH"))
print(os.path.abspath('.'))
"""
#fsl=[x for x in myos.listdir('.') if myos.path.isfile(x) and myos.path.splitext(x)[1]=='.py']
#print(fsl)
#endregion

#region 序列化
"""
import pickle
d = dict(name = "冯小刚", work = "导演", age = 60)
#s = pickle.dumps(d)
f = open("/home/fxgang/doc/f003.txt", "wb")
pickle.dump(d, f)
f.close()

f = open("/home/fxgang/doc/f003.txt", "rb")
d = pickle.load(f)
f.close()
print(d)

with open("/home/fxgang/doc/f003.txt", "rb") as f:
    k = pickle.load(f)
    print(k)
"""
#endregion

#region Json
import  json
d = dict(name = "冯小刚", work = "导演", age = 60)
s = json.dumps(d)
k = json.loads(s)
print(s, k)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        "name":std.name,
        "age":std.age,
        "score":std.score
    }
u = Student("冯小刚", 60, 99.89)
s = json.dumps(u, default= student2dict)
s1 = json.dumps(u, default=lambda o:o.__dict__)
print(s)
print(s1)
#endregion

