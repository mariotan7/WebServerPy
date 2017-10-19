#! /usr/local/bin/python3

from contextlib import closing
import socket


def main():

    host = "127.0.0.1"
    port = 8001
    backlog = 10
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((host, port))
    sock.listen(backlog)
    print("クライアントからの接続を待ちます.")

    conn, address = sock.accept()
    print("クライアント接続.")

    msg = conn.recv(bufsize)
    print(address)

    with open("server_recv.txt", "wb") as fr:
        fr.write(msg)

    with open("server_send.txt", "rb") as fs:
        data = fs.read()
        conn.send(data)

    closing(conn)
    closing(sock)

    print("通信を終了しました.")


if __name__ == "__main__":
    main()
