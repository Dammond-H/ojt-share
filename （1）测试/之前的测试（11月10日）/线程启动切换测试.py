import threading


def show():
    print(threading.currentThread().name)
    print("hello world")


def mainShow():
    print(threading.currentThread().name)
    print("Main thread")

if __name__ == '__main__':
    fileFlag = 0
    thread = threading.Thread(target=show)
    for i in range(1,10):
        if i % 2 == 0:
            if not fileFlag:
                print("执行...")
                fileFlag = 1
                thread.start()
            else:
                show()
        else:
            show()


