import socket
import colorama
from concurrent import futures


def handle(conn):
    while True:
        data = conn.recv(1024).decode()

        if not data:
            break
        print(f'\033[032m received message: {data}\033[0m')
        message = input('--> ')
        conn.send(message.encode())

    print('ok')
    conn.close()


def main():
    host = socket.gethostname()
    port = 8080

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(10)
    with futures.ThreadPoolExecutor(10) as pool:
        while True:
            conn, address = server_socket.accept()
            pool.submit(handle, conn)
            print(f'\033[034m Connection from {address}\033[0m')


if __name__ == '__main__':
    main()
