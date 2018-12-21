import socket
import threading

host  = '127.0.0.1'
port = 5000

server = socket.socket()
server.bind((host,port))
server.listen(10)

list_of_clients = []

def connection(conn):
    while True:
        msg = conn.recv(1024).decode()
        for c in list_of_clients:
            c.send(msg.encode())
while True:
    conn, addr = server.accept()
    conn.send("Welcome to messenger!! ".encode())
    if (conn not in list_of_clients):
        list_of_clients.append(conn)
        threading.Thread(target = connection, args = (conn,)).start()


