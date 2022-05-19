import os

import socket  # Import socket module
#
s = socket.socket()  # Create a socket object
# host = socket.gethostname()  # Get local machine name
host = "localhost"
port = 55555
# Reserve a port for your service.

s.connect((host, port))


path = r"C:\Users\USER\PycharmProjects\FreeCcodeCamp\test2.zip"
f = open(path, 'rb')
print('Sending...')
l = f.read(1000000024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(10000024)
f.close()
s.send(bytes('nothing', encoding="utf-8"))
print("Done Sending")
print(s.recv(10000024).decode("utf-8"))

# s = socket.socket()  # Create a socket object
# # host = socket.gethostname()  # Get local machine name
# host = "localhost"
# port = 55555  # Reserve a port for your service.

# s.connect((host, port))
# s.close()

# Folder
