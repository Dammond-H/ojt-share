import time
import threading

class Test:
    def __init__(self):
        pass

    def file(self):
        print(threading.currentThread().name)
        for i in range(10):
            print("\033[3%s;1m 正在传输文件.. \033[0m" % i)
            time.sleep(1)

        return "finish"
