#!/usr/bin/env python
# coding: utf-8

import threading
import time

from transferFile import Test

class Job(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(Job, self).__init__(*args, **kwargs)
        self.__flag = threading.Event()         # 用于暂停线程的标识
        self.__flag.clear()
        self.__running = threading.Event()      # 用于停止线程的标识
        self.__running.set()                    # 将running设置为True
        self.test = Test()

    def run(self):
        while self.__running.isSet():
            print(threading.currentThread().name)
            self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print("hello world。。。")
            self.__flag.clear()
            # if self.test.file():
            #     self.stop()

    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False

    def alive(self):
        self.__running.set()

def monitor(a):
    print("执行")
    a.run()

if __name__ == '__main__':
    a = Job()
    a.start()
    a.resume()
    a.stop()
    # a.stop()
    # monitor(a)

