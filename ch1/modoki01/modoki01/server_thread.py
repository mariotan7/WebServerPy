import datetime
import threading
import os.path


class ServerThread(threading.Thread):

    def __init__(self, document_root, sock):
        super(ServerThread, self).__init__()

        self.__DOCUMENT_ROOT = document_root
        self.sock = sock

    @property
    def document_root(self):
        return self.__DOCUMENT_ROOT

    def run(self):

        path = None
        ext = None

        with self.sock.makefile() as input_stream:
            line = read_line(input_stream)

            while not line.isspace():

                if (line == ""):
                    break

                if (line.startswith("GET")):
                    path = line.split(" ")[1]
                    root, ext_with_dot = os.path.splitext(path)
                    ext = ext_with_dot.lstrip(".")

                line = read_line(input_stream)

            write_line(self.sock, "HTTP/1.1 200 OK")
            write_line(self.sock, "Date: " + get_date_string_utc())
            write_line(self.sock, "Server: Modoki/0.1")
            write_line(self.sock, "sockection: close")
            write_line(self.sock, "Content-type: " + get_content_type(ext))
            write_line(self.sock, "")

            with open(self.__DOCUMENT_ROOT + path, "rb") as fp:
                self.sock.send(fp.read())


def write_line(stream, line):
    stream.send((line + "\r\n").encode())


def read_line(stream):
    return stream.readline()


def get_date_string_utc():
    now = datetime.datetime.utcnow()
    return "{0:%a, %d %b %Y %H:%M:%S GMT}".format(now)


def get_content_type_map():

    type_map = {}

    type_map["html"] = "text/html"
    type_map["htm"] = "text/html"
    type_map["txt"] = "text/plain"
    type_map["css"] = "text/css"
    type_map["pnt"] = "image/png"
    type_map["jpg"] = "image/jpeg"
    type_map["jpeg"] = "image/jpeg"
    type_map["gif"] = "image/gif"

    return type_map


def get_content_type(ext):

    ret = get_content_type_map()[ext.lower()]

    if ret is None:
        return "application/octet-stream"
    else:
        return ret
