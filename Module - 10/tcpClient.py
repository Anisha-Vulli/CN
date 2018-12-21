# import socket
# import threading

# host  = '127.0.0.1'
# port = 5000
# s = socket.socket()
# s.connect((host,port))
# username = input("Enter user name:")
# # s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# def receiveMsg(s):
#     while True:
#         msg = s.recv(1024).decode()
#         print(msg)

# threading.Thread(target=receiveMsg, args=(s,)).start()
# while True:
#     message = input()
#     msg = username + ": " + message 
#     s.send(msg.encode())  
# s.close() 


import socket
import threading
s=socket.socket()
port=5000
username=input("Enter user name:")
ip="127.0.0.1"
s.connect((ip,port))
def receiveMsg(sock):
    while True:
        msg=sock.recv(1024).decode()
        print(msg)
threading.Thread(target=receiveMsg,args=(s,)).start()
while True:
    tempMsg=input()
    msg=username+'>>'+tempMsg
    s.send(msg.encode())
