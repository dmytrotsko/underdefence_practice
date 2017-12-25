from socket import *
import os

def launchServer():
	host = 'localhost'
	port = 9000

	socket_server = socket(AF_INET, SOCK_STREAM)
	socket_server.bind((host, port))
	socket_server.listen(5)
	path = os.curdir

	while True:
		(client, clientess) = socket_server.accept()
		data = client.recv(5120)
		requested_file = data.split(' ')[1]
		requested_file = requested_file.split('?')[0].rstrip('favicon.ico').rstrip('/').rstrip('\n')
		path = path + '/' + requested_file

		client.send("HTTP/1.1 200 OK\n"
         +"\n" # Important!
         +"<html><body><table><tr><th>"+path+"</th></tr>\n")
		if os.path.isfile(path):
			f = open(path, 'r')
			for line in f.readlines():
				client.send(line + '<br>')
			f.close()
		else:
			for dir in os.listdir(path):
				client.send("<tr><tb>"+"<a href='"+requested_file+"/"+dir+"'>"+dir+"</tb><br>")

		client.shutdown(SHUT_WR)
		client.close()
		print(requested_file)
		path = os.curdir

	socket_server.close()
launchServer()