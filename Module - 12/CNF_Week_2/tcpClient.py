import socket

s = socket.socket()
port = 5000
ip = "127.0.0.1"
s.connect((ip,port))

heading = s.recv(1024).decode()
print(heading)

while True:
    tempMsg = input()
    msg = tempMsg
    s.send(msg.encode())
    ques = s.recv(1024).decode()
    print(ques)
