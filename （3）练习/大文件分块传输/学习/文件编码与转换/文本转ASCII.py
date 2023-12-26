if __name__ == '__main__':
    text = '''特征值并不是连续的，而是离散的，无序的。通常我们需要对其进行特征数字化。
    One-Hot编码，又称为一位有效编码，主要是采用N位状态寄存器来对N个状态进行编码，每个状态都由他独立的寄存器位，并且在任意时候只有一位有效。
    '''
    data = text.encode("utf-8")
    print(data)
    asi = []
    for num in data:
        asi.append(num)
    print(asi[0])
    i = ord("\x89")
    print(i)
    encode = chr(i).encode("utf-8")
    print(encode)