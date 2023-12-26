import threading
import time

def sub():
    count = 1
    while True:
        if count % 10 == 0:
            flag = 1
        print(count)
        count += 1
        time.sleep(0.8)

def par():
    while flag:
        print("执行父进程")
if __name__ == '__main__':
    flag = 0