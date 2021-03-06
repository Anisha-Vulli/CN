import socket

def convert(data) :
    li = data.split(" ")
    if(li[0] == "INR"):
        c = int(li[1])/67

    if(li[0] == "Yen") :
        c = int(li[1])/113.47

    if(li[0] == "Pounds") :
        c = int(li[1])/0.75

    if(li[0] == "Dollars") :
        if(li[-1] == "INR"):
            c = int(li[1])*67
        if(li[-1] == "Yen") :
            c = int(li[1])*113.47
        if(li[-1] == "Pounds") :
            c = int(li[1])*0.75
    return c


def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print('Server started..')

	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode()
		print('Message from: ' + str(addr))
		print('From connect user: ' + str(data))
		conv = convert(data)
		print('sending: ' + str(data))
		s.sendto(str(conv).encode(), addr)
	s.close()

if __name__ == '__main__':
	Main()