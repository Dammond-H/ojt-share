import os,sys
import math
import threading
import time
from concurrent.futures import ThreadPoolExecutor

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

    # return fileCapacity

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

    return "finish"
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
    print("接收完毕开始合并...")
    listdir = os.listdir(os.path.join(filePath))
    tempSize = 0
    for item in listdir:
        tempSize += os.path.getsize(item)
    print(tempSize)
    f = open(os.path.join(filePath,"毕设.docx"),"wb")
    for i in range(len(listdir)):
        fo = open("block%s.txt"%(i+1),"rb")
        while True:
            data = fo.read(1024)
            if not data:
                break
            f.write(data)
    print("执行完毕")

if __name__ == '__main__':
    fileCapacity ,flag= [],0
    print(dirname)
    chunkSize = 1024*1024
    fileName = "9+1605020054黄林强+论文终稿.docx"
    splitFile(fileName)
    filePath = os.path.join(dirname, "文件分割与合并", "合并")
    executor = ThreadPoolExecutor(max_workers=4)
    # 开启线程池，进行文件接收
    '''
    因为频繁的创建线程 销毁线程，非常的浪费资源，所以我们创建线程池，通过线程池就可以重复利用线程。
    '''
    for i in range(len(fileCapacity)):
        submit = executor.submit(recvFile, fileCapacity[i])
    # 阻塞
    executor.shutdown(wait=True)
    joinFile()


