import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)
print('Подключено к серверу', server_address)

message = 'Привет, сервер'
client_socket.sendall(message.encode('utf-8'))

data = client_socket.recv(1024)
print('Получен ответ от сервера', data.decode('utf-8'))

client_socket.close()