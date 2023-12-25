import subprocess
import socket

ip_bind = ("127.0.0.1",9000)
client = socket.socket()
client.connect(ip_bind)
l1 = []
while True:
    option = input("client:")
    client.sendall(bytes(option,encoding="utf-8"))
    server_data_size = client.recv(50)
    print(server_data_size)
    a = str(server_data_size,encoding="utf-8").strip()
    print(a)
    l1 = a.split(":")
    print(l1)
    if l1[0] == "server_data_size":
        client_size_tmp = l1[1]
        print(client_size_tmp)
        client_size = int(client_size_tmp)
        print(type(client_size))
    client.send(bytes("ok",encoding="utf-8"))
    receive_size = 0
    res = ""
    while receive_size < client_size:
        server_data = client.recv(100)
        receive_size += len(server_data)
        res += str(server_data)
    else:
        print(res)
        print("-------reveive down---------")