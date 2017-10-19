#! /usr/local/bin/python3

import socket
import server_thread


def main():
    host = "127.0.0.1"
    port = 8001
    backlog = 10
    DOCUMENT_ROOT = "./"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(backlog)
        print("クライアントからの接続を待ちます.")

        while True:
            conn, address = sock.accept()
            print("クライアント接続.")

            s_thread = server_thread.ServerThread(DOCUMENT_ROOT, conn)
            s_thread.start()


if __name__ == "__main__":
    main()
