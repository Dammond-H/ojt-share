import threading


def get_thread_a(condition):
    with condition:
        condition.wait()
        print("A : Hello B,that's ok")
        condition.notify()
        condition.wait()
        print("A : I'm fine,and you?")
        condition.notify()
        condition.wait()
        print("A : Nice to meet you")
        condition.notify()
        condition.wait()
        print("A : That's all for today")
        condition.notify()


def get_thread_b(condition):
    with condition:
        print("B : Hi A, Let's start the conversation")
        condition.notify()
        condition.wait()
        print("B : How are you")
        condition.notify()
        condition.wait()
        print("B : I'm fine too")
        condition.notify()
        condition.wait()
        print("B : Nice to meet you,too")
        condition.notify()
        condition.wait()
        print("B : Oh,goodbye")


if __name__ == "__main__":
    condition = threading.Condition()
    thread_a = threading.Thread(target=get_thread_a, args=(condition,))
    thread_b = threading.Thread(target=get_thread_b, args=(condition,))
    thread_a.start()
    thread_b.start()