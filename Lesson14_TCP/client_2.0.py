import socket

SRV_HOST = '127.0.0.1'
SRV_PORT = 1234

name = input('Enter name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SRV_HOST, SRV_PORT))

client.send('<{}> has connected'.format(name).encode())

while True:
    message = input('<{}>: '.format(name))
    client.recv(2048).decode()
    if message == 'q':
        client.send('<{}> left chat.'.format(name).encode())
        client.close()
        break
    else:
        client.send(f'<{name}>: {message}'.encode())
