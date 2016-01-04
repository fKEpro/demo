# ch15_02.py
# server socket


import socket


# create tcp/ip socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8091

# bind to the port
server.bind((host, port))
# queue up to 10 clients
server.listen(10)
counter = 0
print('waiting connection from clients...')
while True:
    # establish a connection
    client, address = server.accept()

    counter += 1
    print('a new connection from',str(address))
    message = "welcome, your id=" + str(counter) + "\r\n"
    client.send(message.encode('ascii'))
    client.close()


