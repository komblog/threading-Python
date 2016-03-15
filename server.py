import socket
from thread import start_new_thread

PORT = 4000
BUFF = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(10)

def recv_all(s):
    pesan = ''
    while True:
        buf = s.recv(6)
        if "\r\n" in buf:
            buf = buf.replace("\r\n","")
            pesan+=buf
            return pesan
        pesan+=buf
    return pesan

def handler(data):
    while True:
        text = recv_all(data)
        #balikkan = list(text)
        #balikkan.reverse()
        #coba = join(balikkan)
        if not text : break
        print "Client ",conn," say : ",text
        #print "Setelah dibalikkan : ",coba
        reply = "Terimakasih "+text
        data.send(reply)
    data.close()

print "Menunggu koneksi di PORT : ",PORT
while True:

    data, conn = s.accept()
    print "Terhubung dengan ",conn
    start_new_thread(handler,(data,))
