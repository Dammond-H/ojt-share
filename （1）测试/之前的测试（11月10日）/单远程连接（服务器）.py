from socket import *

ip_port = ("202.193.52.206",8080)
bufSize = 1024
# 生成套接字
udp_server = socket(AF_INET, SOCK_DGRAM)
# 绑定
udp_server.bind(ip_port)
print("服务器启动...")
while True:
    data,addr = udp_server.recvfrom(bufSize)
    print("收到从客户端发送的数据 %s 端口地址为 %s" % (data.decode("utf-8"), addr))

    udp_server.sendto(data.upper(),addr)
