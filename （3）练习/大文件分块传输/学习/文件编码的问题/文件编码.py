# -*- coding: utf-8 -*-
import time,os
import sys


if __name__ == '__main__':
    '''https://blog.csdn.net/q6q6q/article/details/109343085'''
    print(os.path.getsize("test.txt"))
    # with open("统计学习.docx",encoding="utf-8") as fo:
    #     data = fo.read(1024)
    fo = open("遗传算法总结aa.docx","rb")
    asi,temp= [],b""
    while True:
        data = fo.read(1024)
        if not data:
            break
        print(data)
        for item in data:
            # print(type(item))
            print(item,chr(item).encode("utf-8"),end=" ",)
        time.sleep(30)
        # text = data.decode("GB2312","ignore")
        # print(text)
        # for item in text:
        #     i = ord(item)
        #     asi.append(i)
    for data in asi:
        temp += chr(data).encode("utf-8")
    # fi = open("22.docx","wb")
    # fi.write(temp)
    # print(os.path.getsize("22.docx"))
