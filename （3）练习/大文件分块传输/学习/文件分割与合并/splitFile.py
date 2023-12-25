import os,sys
import math
import threading
import time

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 分割文件
def splitFile(fileName):
    fileSize = os.path.getsize(fileName)
    print(fileSize)
    # fileBlocks = math.ceil(fileSize / chunkSize)
    print("可以分割成 %s 个文件块" % math.ceil(fileSize / chunkSize))
    fileRead = open(fileName, "rb")
    readSize ,i,blockSize= 0,0,0
    fileWriter = open("block%s.txt"%(i+1), "wb")
    while readSize < fileSize:
        data = fileRead.read(1024)
        fileWriter.write(data)
        readSize += len(data)
        blockSize += len(data)
        if blockSize == chunkSize:
            fileCapacity.append("block%s.txt" % (i + 1))
            i += 1
            fileWriter.close()
            fileWriter = open("block%s.txt"%(i+1),"wb")
            blockSize = 0

    fileCapacity.append("block%s.txt" % (i + 1))

    return fileCapacity

# 接收文件
def recvFile(fileName):
    print(threading.currentThread().name,"正在处理",fileName)
    # readSize = 0
    # fileSize = os.path.getsize(fileName)
    fileRead = open(fileName, "rb")
    fileWriter = open(os.path.join(filePath,fileName), "wb")
    while True:
        data = fileRead.read(1024)
        if not data:
            fileCapacity.remove(fileName)
            break
        fileWriter.write(data)
    # while True:
    #     if readSize < os.path.getsize(fileName):
    #         print(readSize)
    #         print(fileSize)
    #         data = fileRead.read(1024)
    #         # print(data)
    #         # print(data)
    #         # if not data:
    #         #     fileCapacity.remove(fileName)
    #         #     break
    #         fileWrite = open(os.path.join(filePath,fileName), "wb")
    #         fileWrite.write(data)
    #         readSize += len(data)
    #     else:
    #         fileWrite.close()
    #         break

# 合并文件
def joinFile():
    t = []
    for i in range(4):
        # print(fileCapacity[i])
        thread = threading.Thread(target=recvFile,args=(fileCapacity[i],))
        t.append(thread)
    for temp in t:
        temp.start()
    for temp in t:
        temp.join()
    if len(fileCapacity) == 0:
        print("接收完毕,开始合并")
        f = open(os.path.join(filePath,"计算机网络课件.zip"), "wb")
        listdir = os.listdir(filePath)
        for i in range(len(listdir)):
            while True:
                data = f.read("block%s"%(i+1),"rb")
                if not data:
                    break
                f.write(data)
        print(os.path.getsize(os.path.join(filePath,"计算机网络课件.zip")))
        # tempSize = 0
        # for item in listdir:
        #     tempSize += os.path.getsize(os.path.join(filePath,item))
        # print(tempSize)
    # while True:
    #     pass



if __name__ == '__main__':
    fileCapacity ,flag= [],0
    print(dirname)
    chunkSize = 1024*1024
    fileName = "计算机网络课件.zip"
    splitFile(fileName)
    filePath = os.path.join(dirname, "文件分割与合并", "合并")
    joinFile()

