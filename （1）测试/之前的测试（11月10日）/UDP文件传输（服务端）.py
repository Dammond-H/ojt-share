import os
import socket

count = 0

def transferFile(fileSize):
    print(fileSize)
    f = open("app开发.pdf","wb")
    recvSize = 0
    count = 0
    while True:
        data, addr = s.recvfrom(1024)
        if str(data) != b"end":
            f.write(data)
            print("receive"+ str(count) + 'byte')
            count += 1
        else:
            break
    # while recvSize < fileSize:
    #     try:
    #         data,addr = s.recvfrom(1024)
    #         print(str(count) + 'byte')
    #         f.write(data)
    #         recvSize += len(data)
    #         count += 1
    #     except Exception as e:
    #         if hasattr(e,"reason"):
    #             print(e.reason)
    f.close()
    print("接收完成...")
if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('127.0.0.1',9999)
    s.bind(server_addr)

    print('Bind UDP on 9999...')
    data,addr = s.recvfrom(1024)
    print(data.decode("utf-8"))
    s.sendto("OK".encode("utf-8"),addr)
    fileSize = os.path.getsize("C:/Users/黄林强/Desktop/702984 HTML5 App应用开发教程.pdf")
    transferFile(fileSize)
    # while True:
    #     if count == 0:
    #         data,client_addr = s.recvfrom(1024)
    #         print('connected from %s:%s'%client_addr)
    #         f = open(data, 'wb')
    #     data, client_addr = s.recvfrom(1024)
    #     if str(data) != "b'end'":
    #         f.write(data)
    #         print('recieved '+str(count)+' byte')
    #     else:
    #         break
    #     s.sendto('ok'.encode('utf-8'),client_addr)
    #     count+=1
    # print('recercled'+str(count))
    # f.close()
    # s.close()

    # data, addr = s.recvfrom(1024)
    # print('Received from %s:%s' %addr)
    # s.sendto(b'Hello, %s!' %data, addr)
