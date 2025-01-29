import socket

host = '127.0.0.1'
port = 58202 # arbitrary. pick the port you want
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port)) # pass in tuple with ip and port
sock.listen() # listen for incoming TCP connections
# wait...
connection, address = sock.accept()
message = b''
try:
	while True:
		data = connection.recv(1024)
		if len(data) < 1024: # kind of computationally inefficient... but whatever
			print(f'should be the last packet')
		message += data # handle partial receipts (i.e., len(data) < 1024)
		if not data:
			break # check if no data was sent. not data == b''
except Exception as e:
	print(f"error occured. socket closed.\n{e}")
finally:
	connection.close()

print(f"final message was {len(message)} bytes in length")
to = open('message.txt', 'wb')
to.write(message) # could do better. but this works
to.close()
