import os

if __name__ == '__main__':
    dirname = os.path.dirname(os.path.dirname(__file__))
    filePath = os.path.join(dirname, "测试", "1.txt")
    fileName = os.path.basename(filePath)
    name = os.path.splitext(fileName)[0]
    print(name)
