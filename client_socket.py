
# client socket


import socket

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip/hostname of server
# change this ip address
host = '192.168.0.10'
port = 8091

print('connecting to server...')
client.connect((host, port))
print('connected')

recv = client.recv(1024)
print('received:', recv.decode('ascii'))

client.close()
print('closed')

