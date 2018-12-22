import socket
import threading
import collections

host  = '127.0.0.1'
port = 5000

server = socket.socket()
server.bind((host,port))
server.listen(10)

list_of_clients = []

f = open("data.csv", "r")
#print(f.read())

data = []
for x in f:
    data.append(x)

rollno_dict = {}

for y in data:
    line = y.split(",")
    rollno_dict[line[0]] = [line[1], line[-1].rstrip('\n')]

def connection(conn):
    while True:
        msg = conn.recv(1024).decode()
        print(msg)
        line = msg.split(" ")
        for c in list_of_clients:
            if line[0] == 'mark':
                value = rollno_dict.get(line[-1])
                if line[1] not in rollno_dict:
                    c.send("Person not found".encode())
                else:
                    c.send(value[0].encode())
                    answer = c.recv(1024).decode()
                    if answer == value[-1]:
                        c.send("Attendence marked".encode())
                    else:
                        c.send("Attendence marking failed".encode())
while True:
    conn, addr = server.accept()
    print ('connection from : '+ str(addr))
    conn.send("Welcome to mark Attendence ".encode())
    if (conn not in list_of_clients):
        list_of_clients.append(conn)
        threading.Thread(target = connection, args = (conn,)).start()

