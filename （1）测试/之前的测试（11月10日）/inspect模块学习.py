import inspect

class A:
    def __init__(self):
        pass

    def show(self):
        print("hello")

if __name__ == '__main__':
    print(type(A))
    if inspect.isclass(A):
        print(inspect.isclass(A))
    else:
        print("False")