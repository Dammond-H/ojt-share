import json
import os
from socket import *
# from conf import conf

class socketClient():
    def __init__(self):
        self.port = ("localhost",8686)
        self.bufSize = 1024
        self.updClient = socket(AF_INET, SOCK_DGRAM)
        print("客户端已启动...")

    '接收消息'
    def recvInfo(self):
        data,addr = self.updClient.recvfrom(client.bufSize)
        data = json.loads(data)
        fileName = data.get("fileName")
        fileSize = data.get("fileSize")
        if os.path.exists(fileName):
            print("文件已存在！是否覆盖")
        else:
            self.updClient.sendto("yes".encode("utf-8"),self.port)
        self.receiveContent = 0
        f = open(fileName,"wb")
        while self.receiveContent < fileSize:
            try:
                data,addr = self.updClient.recvfrom(client.bufSize)
            except Exception as e:
                if hasattr(e,"reason"):
                    print(e.reason)
            print("world")
            f.write(data)
            self.receiveContent += len(data)
        f.close()

        print("接收成功...")

    '发送消息'
    def sendInfo(self):
        msg = input(">>")
        self.updClient.sendto(msg.encode("utf-8"),self.port)

if __name__ == '__main__':
    client = socketClient()
    client.updClient.sendto(input(">>").encode("utf-8"),client.port)
    client.recvInfo()

