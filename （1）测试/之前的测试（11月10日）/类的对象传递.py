class A:
    def __init__(self):
        self.x = 1
        self.y = 2

    def show(self):
        print("hello")

class B:
    def __init__(self):
        self.a = A()
        self.z = -1

    def display(self):
        print(type(self.a))
        print(self.a.x)
        print("Python")

if __name__ == '__main__':
    b = B()
    b.display()
    a = A()
    print(a.__dict__)
    print(A.__dict__)