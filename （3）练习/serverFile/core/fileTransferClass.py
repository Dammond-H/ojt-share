import threading

from conf import variable

class fileOperator(threading.Thread):

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
        # 获取socketServer的对象
        self.file = variable.server

    # 线程执行
    def run(self) -> None:
        print("\033[34;1m 线程[%s] 处理文件传输...\033[0m" % threading.currentThread().name)
        while self.__running.isSet():
            # 线程等待
            self.__flag.wait()
            # 文件传输操作
            self.file.transferFiles()

    # 线程挂起
    def suspend(self):
        self.__flag.clear()

    # 线程唤醒
    def awaken(self):
        self.__flag.set()

    # 线程停止
    def stop(self):
        self.__flag.set()
        self.__running.clear()

    # 线程激活
    def alive(self):
        self.__running.set()