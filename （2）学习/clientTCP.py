import socket
ip_port = ("127.0.0.1",8080)

tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(ip_port)

tcp_client.send("hello".encode("utf-8"))
server_msg = tcp_client.recv(1024)
print("收到服务器的消息%s" % server_msg.decode("utf-8"))