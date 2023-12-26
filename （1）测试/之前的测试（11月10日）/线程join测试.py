import threading
import time


def t1(t2):
    count = 1
    while True:
        print("%s 正在刷牙..." % threading.currentThread().name,"count is ",count)
        time.sleep(0.5)

        if count == 5:
            "join() 方法的功能是在程序指定位置，优先让该方法的调用者使用 CPU 资源"
            t2.join()
        count += 1

def t2():
    count = 1
    while True:
        print("%s 正在起床..." % threading.currentThread().name)
        time.sleep(1)
        if count == 10:
            break
        count += 1

def t3():
    while True:
        print("%s 正在吃饭..." % threading.currentThread().name)
        time.sleep(0.4)


if __name__ == '__main__':
    t2 = threading.Thread(target=t2)
    t1 = threading.Thread(target=t1,args=(t2,))
    # t2 = threading.Thread(target=t2)
    t1.start()
    t2.start()
    t3()