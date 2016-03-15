import socket, sys

PORT = 4000
BUFF = 1000

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', PORT))

text = input("Say : ")
c.send(text)
reply = c.recv(BUFF)
print "Server say : "+reply
