import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

server_socket.listen(1)
print('Сервер  слушает на {}:{}:'.format(*server_address))

while True:
    print('Ожидание подключения...')
    client_socket, client_address = server_socket.accept()
    print('Прянято подключение от ', client_address)
    data = client_socket.recv(1024)
    print('Получены данные ', data.decode('utf-8'))

    message = 'Привет, клиент'
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()
