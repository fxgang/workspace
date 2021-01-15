# -*- coding: utf-8 -*-

#region fork
"""
import os
s = "Process (%s) start..." % os.getpid()
print(s)
pid = os.fork()
if pid == 0:
    s = "我是子进程：%s 我的父进程是：%s" % (os.getpid(), os.getppid())
else:
    s = "我：%s创建了一个子进程：%s" % (os.getpid(), pid)
print(s)
"""
#endregion

#region process
"""
import os
from multiprocessing import Process, Pool
from multiprocesslib import run_proc, long_time_task
if __name__ == "__main__":
    print("当前进程：%s" % os.getpid())
    p = Process(target=run_proc, args=("子进程",))
    print("即将启动子进程")
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print("子进程执行完毕！")
    print("=================******=================")
if __name__ == "__main__":
    print("当前进程：%s ... ..." % os.getpid())
    n = 10
    p = Pool(n+1)
    for i in range(n):
        p.apply_async(long_time_task,args=(i,))
    print("等待所有子进程的开始... ...")
    #对Pool对象调用join()方法会等待所有子进程执行完毕
    #调用join()之前必须先调用close()
    #调用close()之后就不能继续添加新的Process了
    p.close()
    p.join()
    print("所有子进程已经完成")
"""
#endregion

#region subprocess
"""
import subprocess
cmd = "nslookup"
args = "www.zg114.com"
r = subprocess.call([cmd, args])
print("Exit Code Is: %s" % r)

print(cmd)
p = subprocess.Popen([cmd], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit
out, err = p.communicate(b"set q=mx\npython.org\n exit]n")
print(out.decode("utf-8"))
print("Exit Code Is: %s" % p.returncode)
"""
#endregion

#region 进程通讯
"""
from multiprocesslib import write, read
from multiprocessing import Queue, Process
if __name__ == "__main__":
    #父进程创建子进程共享队列
    q = Queue()
    pw = Process(target=write, args=(q,))
    rd = Process(target=read, args=(q,))
    #启动写入子进程
    pw.start()
    #启动读取子进程
    rd.start()
    #等待写入进程结束
    pw.join()
    #rd进程为死循环需要强行总之
    rd.terminate()
"""
#endregion

#开始多线程

#region Threading
"""
import threading
from multiprocesslib import caloop
print("主线程：%s开始启动子线程..." % threading.current_thread().name)
t = threading.Thread(target=caloop, name="loopThead")
t.start()
t.join()
print("主线：%s程中发现子线程：%s已经结束了" % (threading.current_thread().name, t.name))
"""
#endregion

#region 线程同步
'''
import threading, time, multiprocessing
#银行存款
balance = 10
#使用锁
lock = threading.Lock()

def chang_it(n):
    """
    先存款,后取款,结果应该为0
    :param n:
    :return:
    """
    global balance
    balance = balance + n
    balance = balance - n

def run_thrad(n):
    """
    线程体方法
    :param n:
    :return:
    """
    for i in range(2000000):
        chang_it(n)

def run_thrad_lock(n):
    """
    线程体方法.线程锁
    :param n:
    :return:
    """
    for i in range(2000000):
        #获取线程锁
        lock.acquire()
        try:
            chang_it(n)
        except:
            print("执行异常...")
        finally:
            #释放线程锁
            lock.release()

print("两个线程改变前：%s" % balance)
t1 = threading.Thread(target=run_thrad, args=(5,))
t2 = threading.Thread(target=run_thrad, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print("两个线程改变后：%s" % balance)
print("==========**********==========")
print("两个锁定线程改变前：%s" % balance)
t1 = threading.Thread(target=run_thrad_lock, args=(5,))
t2 = threading.Thread(target=run_thrad_lock, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print("两个锁定线程改变后：%s" % balance)

print("本机CPU共有:%s个内核！" % multiprocessing.cpu_count())
#endregion

#region 多核测试
def loopx():
    x = 0
    while(True):
        x = x ^ 1
#根据CPU内核数量启动CPU
for i in range(multiprocessing.cpu_count()):
    print("启动线程:%s" % i)
    t = threading.Thread(target=loopx)
    t.start()
'''
#endregion

#region ThreadLock
import threading
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

#region 通过参数传递
def do_sub_task_1(std):
    print("子任务1正在处理...")

def do_sub_task_2(std):
    print("子任务2正在处理...")

def do_task_1(std):
    print("任务1正在处理，调用两个子任务1...")
    do_sub_task_1(std)
    do_sub_task_1(std)

def do_task_2(std):
    print("任务2正在处理，调用两个子任务2...")
    do_sub_task_2(std)
    do_sub_task_2(std)

def process_student(name, age, score):
    #std是局部变量，但是每个函数都要用它，因此必须传进去：
    #每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。
    std = Student(name, age, score)
    do_task_1(std)
    do_task_2(std)
#endregion

#region 通过全局字典

global_dict={}
def do_task_g1():
    # 不传入std，而是根据当前线程在全局字典中查找
    std = global_dict[threading.current_thread()]

def do_task_g2():
    # 不传入std，而是根据当前线程在全局字典中查找
    std = global_dict[threading.current_thread()]

def process_student_g2(name, age, score):
    std = Student(name, age, score)
    # 把std放到全局变量global_dict中
    global_dict[threading.current_thread()] = std
    do_task_g1()
    do_task_g2()
#endregion

#region 通过ThreadLocal
#创建全局ThreadLocal对象
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
#可以理解为全局变量local_std是一个dict，不但可以用local_std.std，还可以绑定其他变量，如local_school.teacher等等。
#ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
local_std = threading.local()

#处理函数
def process_student_ll():
    std = local_std.std
    s = "你好：%s 你已经:%s岁了,你本期的平均成绩是：%0.2f，子线程：%s 处理完成！" % (std.name, std.age, std.score, threading.current_thread().name)
    print(s)

#启动线程
def process_thread_ll(name, age, score):
    local_std.std = Student(name, age, score)
    process_student_ll()

t1 = threading.Thread(target=process_thread_ll, args=("李志强", 120, 99.99))
t2 = threading.Thread(target=process_thread_ll, args=("陈志伟", 100, 85.68))
t3 = threading.Thread(target=process_thread_ll, args=("龙小蝶", 110, 93.88))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
#endregion

#endregion