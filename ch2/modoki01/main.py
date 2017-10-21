#! /usr/local/bin/python3

import socket
import server_thread as s_t
import os.path


def main():
    host = "127.0.0.1"
    port = 8001
    backlog = 10

    DOC_ROOT = os.path.abspath(".")
    ERR_DOC = "./webserver/error_document"
    SERVER = "localhost:8001"

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.bind((host, port))
            sock.listen(backlog)
            print("クライアントからの接続を待ちます.")

            while True:
                conn, address = sock.accept()
                print("クライアント接続.")

                s_thread = s_t.ServerThread(DOC_ROOT, ERR_DOC, SERVER, conn)
                s_thread.start()

    except KeyboardInterrupt:
        print("\n KeyboardInterrupt. exit.")


if __name__ == "__main__":
    main()
