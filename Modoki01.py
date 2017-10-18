#! /usr/local/bin/python3

import socket
import datetime


def get_date_string_utc():
    now = datetime.datetime.utcnow()
    return "{0:%a, %d %b %Y %H:%M:%S GMT}".format(now)


def write_line(stream, line):
    stream.send((line + "\r\n").encode())


def read_line(stream):
    return stream.readline()


def main():
    host = "127.0.0.1"
    port = 8001
    backlog = 10
    DOCUMENT_ROOT = "./"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(backlog)
        print("クライアントからの接続を待ちます.")

        conn, address = sock.accept()
        print("クライアント接続.")

        path = None

        with conn.makefile() as input_stream:
            line = read_line(input_stream)

            while not line.isspace():

                if (line == ""):
                    break

                if (line.startswith("GET")):
                    path = line.split(" ")[1]

                line = read_line(input_stream)

            write_line(conn, "HTTP/1.1 200 OK")
            write_line(conn, "Date: " + get_date_string_utc())
            write_line(conn, "Server: Modoki/0.1")
            write_line(conn, "Connection: close")
            write_line(conn, "Content-type: text/html")
            write_line(conn, "")

            with open(DOCUMENT_ROOT + path, "rb") as fp:
                conn.send(fp.read())

    print("exit.")


if __name__ == "__main__":
    main()
