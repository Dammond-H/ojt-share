import json
from socket import *
# from conf import conf

class socketServer():
    def __init__(self):
        self.port = ("localhost",8686)
        self.bufSize = 1024
        self.updServer = socket(AF_INET, SOCK_DGRAM)
        self.updServer.bind(self.port)
        print("服务器已启动...")

    '接收消息'
    def recvInfo(self):
        print(type(self.updServer))
        data, addr = self.updServer.recvfrom(self.bufSize)
        print("收到客户端发送的消息 %s 端口地址为 %s" % (data.decode("utf-8"), addr))

    '发送消息'
    def sendInfo(self,addr):
        msg = {
            'filePath': 'C:/Users/黄林强/Desktop/近期文档/遗传算法总结（黄林强）.docx', 'fileName':
            '遗传算法总结（黄林强）.docx',
            'fileSize': 1234030
        }
        dumps = json.dumps(msg)
        filePath = msg.get("filePath")
        fileName = msg.get("fileName")
        fileSize = msg.get("fileSize")
        self.updServer.sendto(dumps.encode("utf-8"),addr)
        data,addr = self.updServer.recvfrom(self.bufSize)
        self.sendSize = 0
        f = open(filePath, "rb")
        if data.decode("utf-8") == "yes":
            while self.sendSize < fileSize:
                print("hello")
                fileContent = f.read(self.bufSize)
                self.updServer.sendto(fileContent, addr)
                self.sendSize += len(fileContent)
            f.close()
        print("文件传输成功...")

if __name__ == '__main__':
    server = socketServer()
    data,addr = server.updServer.recvfrom(1024)
    print(data.decode("utf-8"))
    server.sendInfo(addr)


