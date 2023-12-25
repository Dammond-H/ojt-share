from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("localhost",8080))

while True:
    data = input(">>").strip()
    client.send(data.encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(msg)
