'''
What is Net Code?
	- Networking is a huge field, so we will stick to high level concepts that are important for programming.
	- Networking is the concept of two programs communicating across a network. Whether it be from client-client, client-server or even client to ifself.
	- Client -> An end device interfacing with a human.
	- Server -> A device providing a service for clients.
Sockets
	- Sockets are the programming abstractions for connections.
	- They allow us to communicate in a bidirectional manner.
	- Once they are connected or ready to transmit.
	- We can use them to send data and receive data.
	- They implement the common transport protocols TCP and UDP
Socket Methods
	- socket(socket_family, socket_type)
	The constructor creates a new socket.
	- bind((hostname, port))
	Bind take a tuple of a host address and port
	- listen()
	Starts listening for TCP connections
	- accept()
	Accepts a connection when found.(returns new socket)
	- connect((hostname, port))
	Take a tuple of address and port.
	- recv(buffer)
	Try to grab data from a TCP connetion.
	The buffer size determines how many bytes of data to receive at a time
	- send(bytes)
	Attempts to send the bytes given to it.
	- close()
	Close a socket/connection and free the port.
TCP (Transmission Control Protocol) used by Web Browsers, Email, SSH, FTP, etc. -> Example: Capitalize Sentence Program
	- Use TCP to connect and send text to a server then the server replies with a text capitalized.

'''
import socket

def Main():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.bind(("0.0.0.0", 8888))
	s.listen(5)
	print("Server Listening...")
	c, addr = s.accept()
	print("Connection from: " + str(addr))
	while(True):
		data = c.recv(4096).decode('utf-8')
		if not data:
			break
		print("From connected user: " + data)
		data = data.upper()
		print("Sending: " + data + " ...")
		c.send(data.encode('utf-8'))
	s.close()

if(__name__ == '__main__'):
	Main()
