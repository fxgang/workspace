# -*- coding: utf-8 -*-
import time, sys, queue
from multiprocessing.managers import BaseManager

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只有从网上获取Queue，所以注册时只提供名字
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

#连接到服务器，也就是运行服务器的机器
server_addr = "127.0.0.1"
print("连接到服务器: %s..." % server_addr)

#连接端口和验证码要与服务器保持一致
m = QueueManager(address=(server_addr, 5000), authkey=b"abc")

#连接网络
m.connect()

#从服务器上获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列获取任务，并把结果写入到result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("执行任务：%d * %d ..." % (n, n))
        r = "%d * %d = %d" % (n, n, n*n)
        time.sleep(1)
        print("将任务数据结果(%s)放入结果队列..." % r)
        result.put(r)
    except queue.Empty:
        print("任务队列为空...")

#处理结束
print("客户端完成！")