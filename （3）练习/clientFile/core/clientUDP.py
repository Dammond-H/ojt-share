#-*- coding:utf-8 -*-

import os
import threading
import time
from socket import *
from conf import variable
import socketserver

class socketClient():
    def __init__(self,condition):
        self.port = variable.ip_port                #
        self.bufSize = variable.bufSize
        self.udpClient = socket(AF_INET, SOCK_DGRAM)
        self.lock = threading.Lock()
        self.fileThread = threading.Thread(target=self.transferFiles,daemon=True)
        # self.udpClient.bind(self.port)
        self.condition = condition

    "# 接收消息"
    def recvInfo(self):
        self.data, self.addr = self.udpClient.recvfrom(self.bufSize)

        return self.addr, self.data

    "# 发送消息"
    def sendInfo(self,msg):
        if isinstance(msg,str):
            print("transfer",msg)
            self.udpClient.sendto(msg.encode("utf-8"),self.port)
        else:
            pass

    "# 检测文件状态"
    def detectStatus(self,dictData):
        self.fileName = dictData.get("fileName")
        # self.filePath = os.path.join(variable.filePath, self.fileName)
        self.filePath = self.fileName
        print("....",variable.filePath,self.fileName)
        self.fileSize = dictData.get("fileSize")
        # 文件存在
        if os.path.exists(self.filePath):
            '待实现'
            # self.udpClient.sendto("800".encode("utf-8"),self.port)

            return False
            # return self.addr, self.data
        # 不存在
        else:
            print("文件不存在...")
            self.udpClient.sendto("200".encode("utf-8"), self.port)

            return True

    "传输文件"
    def transferFiles(self):
        self.condition.acquire()
        # self.condition.wait()
        print("开始接收文件...")
        print("文件名为 %s 文件大小为 %s" % (self.fileName,self.fileSize))
        self.count = 1
        f = open(self.filePath,"wb")

        while True:
            # print("这是等待吗？...")
            data,addr = self.udpClient.recvfrom(self.bufSize)
            if str(data) != "b'end'":
                f.write(data)
                variable.receiveSize += len(data)
                print("receive to "+str(self.count)+" bytes")
                # 重新置为0
                # conf.receiveSize = 0
            else:
                # f.close()
                if variable.receiveSize < self.fileSize:
                    # print("丢包率：%s" % (conf.receiveSize / self.fileSize)*100)
                    self.retransmitFile()
                break
            # conf.receiveSize += len(data)
            self.count += 1

        self.udpClient.sendto("400".encode("utf-8"),self.port)
        # f.close()
        variable.fileTransferThread.stop()
        variable.fileTransferThread.suspend()

        self.condition.notify()
        self.condition.release()
        '方式二'
        # while self.receiveSize < self.fileSize:
        #     data, addr = self.udpClient.recvfrom(self.bufSize)
        #     print("接收内容", data)
        #     f.write(data)
        #     self.receiveSize += len(data)

        # while True:
        #     while self.receiveSize < self.fileSize:
        #         data,addr = self.udpClient.recvfrom(self.bufSize)
        #         print("接收内容",data)
        #         f.write(data)
        #         self.receiveSize += len(data)
        #     break

        # while self.sendSize < self.fileSize:
        #     fileContent = f.write(self.bufSize)
        #     self.udpClient.sendto(fileContent.encode("utf-8"),self.addr)
        #     self.sendSize += len(fileContent)
        # f.close()
        # print("文件接收成功...")

    '重传文件'
    def retransmitFile(self):
        print("\033[35;1m UDP传输中出现丢包，执行重传...\033[0m")
        while True:
            # 接收的文件小于文件大小，直接重传
            if variable.receiveSize < self.fileSize:
                # print("丢包率：%s " % ((self.fileSize - conf.receiveSize) / self.fileSize))
                self.udpClient.sendto(str(os.path.getsize(self.filePath)).encode("utf-8"),self.port)
                # 文件尾部追加
                f = open(self.filePath,"ab")
                while True:
                    data, addr = self.udpClient.recvfrom(self.bufSize)
                    if str(data) != "b'end'":
                        f.write(data)
                        variable.receiveSize += len(data)
                        print("receive to " + str(self.count) + " bytes")
                    else:
                        break
                    self.count += 1
                f.close()
            else:
                break
