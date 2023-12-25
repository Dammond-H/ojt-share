import numpy as np

# 转换成二进制
def toASCII(text):
    asi ,i= [],0
    for t in text:
        temp = []
        for item in t:
            temp.append(ord(item))
        asi.append(temp)

    maxLength = max([len(l)] for l in asi)
    for l in asi:
        if len(l) < maxLength[0]:
            for i in range(maxLength[0] -len(l)):
                l.append(32)
    return asi

# 校验块
def testBlock():
    b = np.identity(3)
    ones = np.ones((2, 3))
    for i in range(1,ones.shape[0]):
        for j in range(ones.shape[1]):
            ones[i][j] = (i+1)**(j)
    b = np.vstack((b, ones))

    return b

# 损失块
def loseBlock(asi,b,store):
    b = np.delete(b,1,axis=0)
    # asi = np.delete(asi,1,axis=0)
    store = np.delete(store,1,axis=0)
    b = b[0:asi.shape[0],:]
    store = store[0:asi.shape[0],:]
    print(b)
    invB = np.linalg.inv(b)
    data = np.dot(invB[1],store)


    return data

    # asi = np.array(asi)
    # dot = np.dot(b,asi)
    # print(dot)


# 恢复块
def restoreBlock(asi,b):
    asi = np.array(asi)
    store = np.dot(b, asi)
    data = loseBlock(asi,b,store)
    text = b""
    for item in data:
        temp = chr(int(item)).encode("utf-8")
        if temp != b" ":
            text += chr(int(item)).encode("utf-8")
    f = open("文件恢复.txt","wb")
    f.write(text)

if __name__ == '__main__':
    np.set_printoptions(suppress=True)
    text = []
    text1 = "特征值并不是连续的，而是离散的，无序的。"
    text2 = "通常我们需要对其进行特征数字化。"
    text3 = "One-Hot编码，又称为一位有效编码，主要是采用N位状态寄存器来对N个状态进行编码，每个状态都由他独立的寄存器位，并且在任意时候只有一位有效。"
    text.append(text1)
    text.append(text2)
    text.append(text3)
    asi = toASCII(text)
    b = testBlock()
    restoreBlock(asi,b)
    # loseBlock(asi,b)