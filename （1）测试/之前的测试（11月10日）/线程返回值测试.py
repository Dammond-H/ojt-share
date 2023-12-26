import threading

def show():
    print("this is threading...")
    return True

def getThreading():
    return show()

if __name__ == '__main__':
    thread = threading.Thread(target=show)
    thread.start()
    thread.join()
    print(getThreading())