import socket

SRV_HOST = '127.0.0.1'
SRV_PORT = 7897

name = input('Enter name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SRV_HOST, SRV_PORT))
client.send('{} has connected'.format(name).encode('utf-8'))

while True:
    message = input('{}: '.format(name))
    client.recv(2048).decode('utf-8')
    client.send('{0}: {1}'.format(name, message).encode('utf-8'))
