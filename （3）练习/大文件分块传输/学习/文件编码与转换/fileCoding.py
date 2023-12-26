import io
import sys
import unicodedata
import binascii

type = sys.stdout.encoding

if __name__ == '__main__':
    '''https://bbs.csdn.net/topics/396977243'''

    information = "黄林强 22 学生"
    encode = information.encode("utf-8")
    # f = open("abc.txt","wb")
    # f.write(encode)
    fo = open("abc.txt", "rb")
    data = fo.read(1024)
    print(data)
    # print(data.decode("gbk"))
    for temp in data.decode("gbk",errors="ignore"):
        print(ord(temp),end=" ")
        print(chr(ord(temp)).encode("gbk"),end=" ")

    # print(encode)
    # asi = []
    # for i in encode:
    #     asi.append(i)
    # print(len(asi))
    # s = bytes(chr(asi[0]),encoding='utf-8')
    # print(s)
    # print("22".encode("utf-8"))
