import socket
ip_port = ("127.0.0.1",8080)
back_log = 5

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
print("正在等待客户端的连接...")
conn,addr = tcp_server.accept()

receive_msg = conn.recv(1024)
print("客户端发送的消息%s" % receive_msg)

conn.send(receive_msg.upper())

conn.close()
tcp_server.close()
