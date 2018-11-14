import socket

HOST = '192.168.1.85'  # The server's hostname or IP address
PORT = 9876      # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.sendall('Hello, world')

    print('hello world')
    #data = s.recv(1024)

#print('Received', repr(data))