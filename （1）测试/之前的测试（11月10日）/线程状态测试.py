import threading


def show():
    print("当前%s正在运行" % threading.currentThread().name)


if __name__ == '__main__':
    thread = threading.Thread(target=show)
    if thread.is_alive():
        print(thread.is_alive())
    else:
        print("没有启动...")


    thread.start()
    if thread.is_alive():
        print(thread.is_alive())
    else:
        print("没有启动...")
    thread.join()
    print("结束...")
