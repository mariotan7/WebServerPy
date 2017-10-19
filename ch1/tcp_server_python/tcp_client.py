#! /usr/local/bin/python3

from contextlib import closing
import socket


def main():

    host = "127.0.0.1"
    port = 8001
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with closing(sock):
        sock.connect((host, port))

        with open("client_send.txt", "rb") as fs:
            data = fs.read()
            sock.send(data)

        with open("client_recv.txt", "wb") as fs:
            msg = sock.recv(bufsize)
            fs.write(msg)


if __name__ == "__main__":
    main()
