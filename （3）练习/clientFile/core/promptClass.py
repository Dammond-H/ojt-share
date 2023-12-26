import threading
import time

from conf import variable

class promptOperator(threading.Thread):

    def __init__(self):
        super().__init__()
        # 用于线程挂起的标志
        self.__flag = threading.Event()
        # self.__flag.set()
        # 挂起状态
        self.__flag.clear()
        # 用于线程停止的标志
        self.__running = threading.Event()
        self.__running.set()
        self.signal = False
        self.count = 1

    # 线程执行
    def run(self) -> None:
        print("\033[35;1m 线程[%s] 处理提示框...\033[0m" % threading.currentThread().name)
        while self.__running.isSet():
            if self.count >0:
                self.__flag.wait()
                variable.prompt.handlePromptMessageEvent(self)
            self.count -= 1
            # self.__flag.clear()


    # 线程挂起
    def suspend(self):
        self.__flag.clear()

    # 线程唤醒
    def awaken(self):
        self.signal = True
        self.__flag.set()

    # 线程停止
    def stop(self):
        self.__flag.set()
        self.__running.clear()


    # 线程激活
    def alive(self):
        self.count = 1
        self.__running.set()

