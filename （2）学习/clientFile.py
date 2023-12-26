import subprocess
import socket
ip_bind = ("127.0.0.1",9000)
server = socket.socket()
server.bind(ip_bind)
server.listen(1)
print("server is waiting........")
conn,add = server.accept()
print("server is connected client")
while True:
    client_data = conn.recv(50)
    a = subprocess.Popen(str(client_data,encoding="utf-8"),stdout=subprocess.PIPE)
    b = a.stdout.read()
    server_data_size = "server_data_size:" + str(len(b))
    conn.sendall(bytes(server_data_size,encoding="utf-8"))
    client_ack = conn.recv(10)
    if str(client_ack,encoding="utf-8") == "ok":
        conn.sendall(b)