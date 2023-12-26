import os
import time

if __name__ == '__main__':
    asi ,count = [],0
    fo = open("1.txt","rb")
    print(os.path.getsize("1.txt"))
    print()
    while True:
        data = fo.read(1024)
        if not data:
            break
        for num in data:
            asi.append(num)
    temp = b""
    f = open("test.txt", "wb")
    # s = ord("\n")
    # print(s)
    print(len(asi))
    for num in asi:
        # chr(int(data)).encode("latin1")
        temp += chr(num).encode("latin1")
        print(temp,len(temp))
        # print(len(temp))
        time.sleep(1)
        count += 1
        # if len(temp)
    #     if len(temp):
    #        f.write(temp)
    #        temp = b""
    # print(len(temp))
    # f.write(temp)
    # print(os.path.getsize("test.txt"))
    dirname = os.path.dirname(os.path.dirname(__file__))

