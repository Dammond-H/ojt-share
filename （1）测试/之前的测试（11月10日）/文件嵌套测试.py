def A():
    print("这是主函数...")
    return B()

def B():
    print("这是次函数...")
    return C()

def C():
    print("这是次次函数...")
    return "that's all..."

if __name__ == '__main__':
    msg = A()
    print(msg)