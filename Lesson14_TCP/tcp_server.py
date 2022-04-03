import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7897

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_sock.bind((SERVER_HOST, SERVER_PORT))
srv_sock.listen(4)

name = input('Enter name: ')

connect, address = srv_sock.accept()
print('Received connection from', address)

data = connect.recv(2048).decode('utf-8')
print(data + ' has connected')
connect.send(name.encode('utf-8'))

while True:
    message = input('Text message: ')
    connect.send(message.encode('utf-8'))
    message = connect.recv(2048).decode('utf-8')
    print(data, ':', message)
    if message == 'exit':
        break
