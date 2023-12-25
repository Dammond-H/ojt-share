import ctypes
import threading
from time import sleep


def kill(thread):
    print("执行...")
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident),ctypes.py_object(SystemExit))

def show():
    print(threading.currentThread().name)
    for i in range(0,5):
        print(i)
    sleep(1)

if __name__ == '__main__':
    while True:
        thread = threading.Thread(target=show)
        # print(thread.is_alive())
        if not thread.is_alive():
            print("%s" % threading.currentThread().name)
            thread.start()
            # print(thread.is_alive())
            thread.join()
