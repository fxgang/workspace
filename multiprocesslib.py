# -*- coding: utf-8 -*-
import random, time, os, threading
from multiprocessing import Queue
def run_proc(name):
    """
    进程运行
    :param name:
    :return:
    """
    s = "运行子进程：%s 进程ID：%s" % (name, os.getpid())
    s = s + "-->" + __name__
    print(s)

def long_time_task(name):
    """
    长时间任务
    :param name:
    :return:
    """
    print("Run Task %s (%s)... ..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*10)
    end = time.time()
    print("Task %s runs %0.2f seconds" % (name, end - start))

def write(q):
    """
    向队列写入数据
    :param q: 等待写入数据的队列
    :return:
    """
    start = ord('A')
    end = ord('z') + 1
    l=[chr(x) for x in range(start, end)]
    print("写入进程，进程ID：%s" % os.getpid())
    for v in l:
        print("写入进程，正在向队列写入数据：%s" % v)
        q.put(v)
        time.sleep(random.random())

def read(q):
    """
    从队列读取数据
    :param q:
    :return:
    """
    print("读取进程，进程ID：%s" % os.getpid())
    while(True):
        v = q.get(True)
        print("读取进程，正在从队列读取数据：%s" % v)

def caloop():
    """
    线程方法
    :return:
    """
    print("线程：%s正在运行..." % threading.current_thread().name)
    n = 0
    while(n < 10):
        n = n + 1
        print("线程： %s >>> %s >>>>>>" % (threading.current_thread().name, n))
        time.sleep(random.random()*5)
    print("线程：%s执行完成... ..." % threading.current_thread().name)