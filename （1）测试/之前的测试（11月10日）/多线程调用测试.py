import threading
import time

def show():
    count = 1
    lock.acquire()
    while True:
        print("%s 执行我哦..." % threading.currentThread().name)
        time.sleep(1)
        count += 1
        if count % 5 == 0:
            lock.notify()
            lock.wait()
    lock.release()

def sendTo():
    lock.acquire()
    # lock.wait()
    count = 1
    while True:
        print("%s 开始计算..." % threading.currentThread().name)
        time.sleep(2)
        count += 1
        if count % 5 == 0:
            lock.notify()
            lock.wait()
    lock.release()

def command():
    while True:
        print("%s 主线程不要面子啊..." % threading.currentThread().name)
        time.sleep(3)

if __name__ == '__main__':
    start = time.time()
    end = 0
    lock = threading.Condition()
    thread = threading.Thread(target=show)
    threading_thread = threading.Thread(target=sendTo)
    thread.start()
    # time.sleep(5)
    threading_thread.start()
    command()
    thread.join()
    threading_thread.join()