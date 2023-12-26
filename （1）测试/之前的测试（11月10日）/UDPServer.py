import socket

count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1',9999)
s.bind(server_addr)

print('Bind UDP on 9999...')
while True:
    if count == 0:
        data,client_addr = s.recvfrom(1024)
        print('connected from %s:%s'%client_addr)
        f = open(data, 'wb')
    data, client_addr = s.recvfrom(1024)
    if str(data) != "b'end'":
        f.write(data)
        print('recieved '+str(count)+' byte')
    else:
        break
    # print("这里执行吗？")
    # s.sendto('ok'.encode('utf-8'),client_addr)
    count+=1
print("这里执行吗？")
s.sendto('ok'.encode('utf-8'),client_addr)
print('recercled'+str(count))
f.close()
s.close()

    # data, addr = s.recvfrom(1024)
    # print('Received from %s:%s' %addr)
    # s.sendto(b'Hello, %s!' %data, addr)
