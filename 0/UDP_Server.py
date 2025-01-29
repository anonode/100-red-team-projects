import socket

host = '127.0.0.1'
port = 58203

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# UDP (User Datagram Protocol), therefore: socket.SOCK_DGRAM
sock.bind((host, port))

message = b''
try:
	while True:
		data, address = sock.recvfrom(1024)
		message += data
		if not data:
			break
except Exception as e:
	print(f"Exception occured. Socket closed.\n{e}")
finally:
	sock.close()

to = open('message.txt', 'wb')
to.write(message)
to.close()
