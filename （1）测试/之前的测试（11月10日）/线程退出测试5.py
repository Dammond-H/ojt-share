import threading

def show():
    pass

if __name__ == '__main__':
    thread = threading.Thread(target=show)
    thread._stop()