import socket
import os
import time

def Get_FilePath_FileName_FileExt(filename):
    filepath, tempfilename = os.path.split(filename)
    shotname, extension = os.path.splitext(tempfilename)
    return filepath, shotname, extension

def transferFile(fileName,fileSize):
    f = open(fileName,"rb")
    sendSize = 0
    count = 0
    while True:
        data = f.read(1024)
        if str(data) != "b''":
            s.sendto(data, client_addr)
            print("send" + str(count) + 'byte')
            count += 1
        else:
            s.sendto('end'.encode('utf-8'), client_addr)
            break
    # while sendSize < fileSize:
    #     data = f.read(1024)
    #     s.sendto(data,client_addr)
    #     print(str(count) + 'byte')
    #     count += 1
    #     sendSize += len(data)
    f.close()
    print("传输完毕...")

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    filename = input('please enter the filename you want to send:\n')
    # filepath, shotname, extension = Get_FilePath_FileName_FileExt(filename)

    client_addr = ('127.0.0.1',9999)
    fileSize = os.path.getsize(filename)
    s.sendto("OK".encode("utf-8"),client_addr)
    data,addr = s.recvfrom(1024)
    print(data.decode("utf-8"))

    transferFile(filename,fileSize)
    # count = 0
    # flag = 1
    # while True:
    #     if count == 0:
    #         data = bytes(shotname+extension, encoding = "utf8")
    #         start = time.time()
    #         s.sendto(data,client_addr)
    #     data = f.read(1024)
    #     if str(data) != "b''":
    #         s.sendto(data,client_addr)
    #         print(str(count)+'byte')
    #
    #     else:
    #         s.sendto('end'.encode('utf-8'),client_addr)
    #         break
    #     data, server_addr = s.recvfrom(1024)
    #     count+=1
    # print('recircled'+str(count))
    # s.close
    # end = time.time()
    # print('cost'+str(round(end-start,2))+'s')
    # for data in [b'Michael',b'Tracy',b'Sarah']:
    #     s.sendto(data,('127.0.0.1',9999))
    #     print(s.recv(1024).decode('utf-8'))
    # s.close()

