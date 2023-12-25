#-*- coding:utf-8 -*-
import pickle
import struct
import numpy as np
import chardet

def recovery():
    pass

def lose():
    pass

if __name__ == '__main__':
    # 文字转ASCII
    file = open("block4.txt", "rb")
    readline = file.read(1024)
    print(readline.decode("gbk",errors="ignore"))
    # text = file.readline().decode("utf-8", errors="ignore")
    # print(text.encode("gbk",errors="ignore"))
    ord1 = ord("黄")
    print(ord1)
    s = chr(ord1)
    print(s)


