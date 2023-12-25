#!/usr/bin/env python
# coding: utf-8
import random
import threading
import time
from transferFile import Test

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()              # 用于暂停线程的标识
        self.__flag.set()                            # 设置为True
        self.__running = threading.Event()           # 用于停止线程的标识
        self.__running.set()                         # 将running设置为True
        self.test = Test()

    def run(self):
        while self.__flag.isSet():
            # print(self.__flag)
            # self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            # print(self.__flag)
            # time.sleep(3)
            # 执行文件传输
            if self.test.file():
                # 挂起
                self.pause()

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()       # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()             # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False

def mainShow(job):
    count = 1
    while True:
        randint = random.randint(0, 9)
        number = random.randint(0,100000)
        print("\033[3%s;1m 睡不着，开始猜数...%s\033[0m" %(int(randint),number))
        if count % 5 == 0:
            print("执行...")
            job.resume()
        count += 1
        time.sleep(1)

if __name__ == '__main__':
    job = Job()
    print(job.temp.isSet())
    job.resume()
    print(job.temp.isSet())