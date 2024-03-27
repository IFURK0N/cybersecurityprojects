import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 5050))
serversocket.listen(5) # become a server socket, maximum 5 connections
print("Ready")
while True:
    connection, address = serversocket.accept()
    print("Ready")
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        break