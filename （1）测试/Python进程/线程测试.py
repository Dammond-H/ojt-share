import threading

class Test(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self) -> None:
        print("hello")

if __name__ == '__main__':
    test = Test()
    test.start()