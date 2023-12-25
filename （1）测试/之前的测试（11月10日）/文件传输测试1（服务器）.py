from socket import *

ip_port = ("127.0.0.1",8080)
bufSize = 1024

s = socket(AF_INET, SOCK_DGRAM)
s.bind(ip_port)
while True:
    data,addr = s.recvfrom(1024)
    print("data>",data)
    msg = input(">>")
    s.sendto(msg.encode("utf-8"), addr)

