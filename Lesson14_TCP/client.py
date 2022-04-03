import socket

SRV_HOST = '127.0.0.1'
SRV_PORT = 7897

name = input("Enter name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SRV_HOST, SRV_PORT))
client.send(name.encode('utf-8'))
client_name = client.recv(2048).decode('utf-8')

print(client_name, 'has connected')

while True:
    message = (client.recv(2048).decode('utf-8'))
    print(client_name, ':', message)
    message = input('Text message: ')
    client.send(message.encode())
    if message == 'exit':
        break


