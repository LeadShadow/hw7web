import socket
import colorama


def client():
    host = socket.gethostname()
    port = 8080

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input('--> ')

    while message.lower().strip() != 'end':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f'\033[032m received message: {data}\033[0m')
        message = input('--> ')

    print('ok')
    client_socket.close()


if __name__ == '__main__':
    client()
