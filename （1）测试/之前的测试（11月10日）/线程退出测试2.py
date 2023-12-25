import ctypes
import inspect
import threading
import time


def _async_raise(tid, exctype):
    print(type(tid))
    print("\033[36;1m线程 %s 结束...\033[0m" % threading.currentThread().name)
    # 把tid类型转成C_long类型
    tid = ctypes.c_long(tid)
    print(type(tid))
    # 判断是否为class
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
    print(thread.ident)
    # print(res)
    # # 结束进程
    # ctypes.pythonapi.PyThreadState_SetAsyncExc None)
    # if res == 0:
    #     raise ValueError("invalid thread id")
    # elif res != 1:
    #     ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
    #     raise SystemError("PyThreadState_SetAsyncExc(tid, failed")

# 停止线程
def stop_thread(thread):
    print(thread.ident)
    print(type(SystemExit))
    # thread.ident返回一个启动线程的标识符，未启动为None
    # SystemExit 这基本上意味着你的程序有一种行为，你想停止它并引发一个错误。
    _async_raise(thread.ident, SystemExit)

def show():
    print("\033[34;1m线程 %s 启动...\033[0m" % threading.currentThread().name)
    print("hello")

if __name__ == '__main__':
    thread = threading.Thread(target=show)
    # print(thread.ident)
    thread.start()
    thread.join()
    stop_thread(thread)
    time.sleep(5)
    thread.start()
