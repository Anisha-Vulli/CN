import socket

def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.connect((host, port))

	message = input("-> ")
	while message != 'q':
		s.send(str.encode(message))
		data = s.recv(1024)
		print ('Received from server: ' + data.decode())
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	Main()
