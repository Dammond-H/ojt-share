from socket import *
ip_port = ("202.193.52.206",8080)
bufSize = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

print("客户端启动...")
while True:
    msg = input(">>")
    udp_client.sendto(msg.encode("utf-8"),ip_port)
    server_msg,addr = udp_client.recvfrom(bufSize)
    print("收到服务器发送来的数据 %s 端口IP %s" % (server_msg.decode("utf-8"),addr))
