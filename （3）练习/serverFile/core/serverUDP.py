#-*- coding:utf-8 -*-

import json
import os
import threading
import time
from socket import *
from conf import variable
import socketserver

class socketServer():
    def __init__(self,condition):
        self.port = variable.ip_port
        self.bufSize = variable.bufSize
        self.udpServer = socket(AF_INET, SOCK_DGRAM)
        self.udpServer.bind(self.port)
        self.fileThread = threading.Thread(target=self.transferFiles,daemon=True)
        self.condition = condition
        # self.sendSize = 0

    "# 接收消息"
    def recvInfo(self):
        self.data,self.addr =self.udpServer.recvfrom(self.bufSize)
        print("data",self.data)

        return self.addr,self.data

    "# 发送消息"
    def sendInfo(self,msg):
        # 普通消息的传输
        if isinstance(msg,str):
            print("普通文本传输a...")
            self.udpServer.sendto(msg.encode("utf-8"), self.addr)
        # 文件、视频传输
        else:
            print("这是要传输文件a...")
            self.filePath = msg.get("filePath")
            self.fileName = msg.get("fileName")
            self.fileSize = msg.get("fileSize")
            jsonData = json.dumps(msg)
            # 给对方发送文件信息（文件大小、文件名等）
            self.udpServer.sendto(jsonData.encode("utf-8"),self.addr)
            # 接收客户端发送来的状态信息
            # data,addr = self.udpServer.recvfrom(1024)
            # 200状态码代表开始发送
            # if self.data.decode("utf-8") == "200":
            #     self.filePath = msg.get("filePath")
            #     self.fileName = msg.get("fileName")
            #     self.fileSize = msg.get("fileSize")
            #     self.fileThread.start()
            #     self.fileThread.join()

            # self.transferFiles(msg)
            # print(json.loads(msg))
            # self.udpServer.sendto(json.loads(msg).encode("Utf-8"), self.addr)
        # self.data, self.addr = self.udpServer.recvfrom(self.bufSize)
        # print("收到从客户端发送的数据 %s 端口地址为 %s" % (self.data.decode("utf-8"), self.addr))

    "# 检测状态"
    '''def detectStatus(self, dictData):
        self.filePath = dictData.get("filePath")
        self.fileName = dictData.get("fileName")
        self.fileSize = dictData.get("fileSize")
        if os.path.exists(self.fileName):
            pass'''

    "传输文件"
    def transferFiles(self):
        print("%s 执行传输文件" % threading.currentThread().name)
        # 获取锁
        self.condition.acquire()
        print("开始传输文件...")
        print("文件所在位置 %s" % self.filePath)
        print("文件名为 %s 文件大小为 %s" % (self.fileName, self.fileSize))
        # filePath = msg.get("filePath")
        # fileName = msg.get("fileName")
        # fileSize = msg.get("fileSize")
        f = open(self.filePath,"rb")
        # receive_size = 0
        self.count = 1
        # while True:
        #     try:
        #         if conf.sendSize < self.fileSize:
        #             data = f.read(self.bufSize)
        #             self.udpServer.sendto(data, self.addr)
        #             print("send to %s bytes" % self.count)
        #             conf.sendSize += len(data)
        #             self.count += 1
        #         else:
        #             break
        #     except Exception as e:
        #         print(e)
        #
        # f.close()

        while True:
            try:
                data = f.read(self.bufSize)
                # 字节->b''->已发送完数据
                if str(data) != "b''":
                    self.udpServer.sendto(data,self.addr)
                    # time.sleep(0.1)
                    # 设置文件已经发送的大小
                    variable.sendSize += len(data)
                    print("Send to "+str(self.count)+" bytes")
                else:
                    # # 重新置为0
                    # conf.sendSize = 0
                    self.udpServer.sendto("end".encode("utf-8"),self.addr)
                    clientResponse = self.retransmitFile()
                    break
                self.count += 1
            except Exception as e:
                print(e)
        # clientResponse,addr = self.udpServer.recvfrom(self.bufSize)
        # f.close()
        print("clientResponse:",clientResponse)

        variable.fileTransferThread.stop()
        variable.fileTransferThread.suspend()

        self.condition.notify()
        self.condition.release()

        '方式二'
        # while self.sendSize < self.fileSize:
        #     fileContent = f.read(self.bufSize)
        #     print("传输内容:", fileContent)
        #     self.udpServer.sendto(fileContent, self.addr)
        #     # self.udpServer.sendto(fileContent.encode("utf-8"),self.addr)
        #     self.sendSize += len(fileContent)


        # while True:
        #     while self.sendSize < self.fileSize:
        #         fileContent = f.read(self.bufSize)
        #         print("传输内容:",fileContent)
        #         self.udpServer.sendto(fileContent, self.addr)
        #         # self.udpServer.sendto(fileContent.encode("utf-8"),self.addr)
        #         self.sendSize += len(fileContent)
        #     break
        # f.close()
        # print("文件传输成功...")
            # self.udpServer.sendto(self.data.upper(), self.addr)

    '重传文件'
    def retransmitFile(self):
        print("出现丢包，执行重传...")
        while True:
            clientResponse, addr = self.udpServer.recvfrom(self.bufSize)
            # print("客户端say:已接收文件大小%s" % clientResponse.decode("utf-8"))
            # 非400执行重传
            if clientResponse.decode("utf-8") != "400":
                f = open(self.filePath, "rb")
                # 客户端已发送的数据
                hasSend = int(clientResponse.decode("utf-8"))
                # 找到重传的位置
                f.seek(hasSend)
                # 已经传输的大小
                variable.sendSize = hasSend
                while True:
                    data = f.read(self.bufSize)
                    # 字节->b''->已发送完数据
                    if str(data) != "b''":
                        self.udpServer.sendto(data, self.addr)
                        # 设置文件已经发送的大小
                        variable.sendSize += len(data)
                        print("Send to " + str(self.count) + " bytes")
                    else:
                        self.udpServer.sendto("end".encode("utf-8"), self.addr)
                        break
                    self.count += 1
                f.close()
            # # 接收的文件小于文件大小，直接重传
            # clientResponse,addr = self.udpServer.recvfrom(self.bufSize)
            # print("客户端已接收大小",hasSend)
            # if clientResponse.decode("utf-8") != "400":
            #     f = open(self.filePath, "rb")
            #     hasSend = int(clientResponse.decode("utf-8"))
            #     f.seek(hasSend)
            #     conf.sendSize = hasSend
            #     while True:
            #         data = f.read(self.bufSize)
            #         # 字节->b''->已发送完数据
            #         if str(data) != "b''":
            #             self.udpServer.sendto(data, self.addr)
            #             # time.sleep(0.1)
            #             # 设置文件已经发送的大小
            #             conf.sendSize += len(data)
            #             print("Send to " + str(self.count) + " bytes")
            #         else:
            #             break
            #         self.count += 1
            else:
                return clientResponse.decode("utf-8")
