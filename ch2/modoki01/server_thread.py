import threading
import os.path

import utility as utl
import send_response as res
import my_url_decoder as url


class ServerThread(threading.Thread):

    def __init__(self, document_root, error_document, server_name, sock):
        super(ServerThread, self).__init__()

        self.__DOCUMENT_ROOT = document_root
        self.__ERROR_DOCUMENT = error_document
        self.__SERVER_NAME = server_name

        self.sock = sock

    @property
    def document_root(self):
        return self.__DOCUMENT_ROOT

    @property
    def error_document(self):
        return self.__ERROR_DOCUMENT

    @property
    def server_name(self):
        return self.__SERVER_NAME

    def run(self):

        path = None
        ext = None
        host = None

        with self.sock.makefile() as input_stream:
            line = utl.read_line(input_stream)

            while not line.isspace():

                if line == "":
                    break

                if line.startswith("GET"):
                    path = url.decode(line.split(" ")[1], "UTF-8")
                    root, ext_with_dot = os.path.splitext(path)
                    ext = ext_with_dot.lstrip(".")

                elif line.startswith("HOST:"):
                    host = line[len("HOST:"):]

                line = utl.read_line(input_stream)

            if path is None :
                return

            if path.endswith("/"):
                path += "index.html"
                ext = "html"

            path_obj = self.document_root + path

            if os.path.exists(path_obj):
                real_path = os.path.abspath(path_obj)

            else :
                res.send_not_found_response(self.sock, self.error_document)
                return

            if not real_path.startswith(self.document_root):
                res.send_not_found_response(self.sock, self.error_document)
                return

            elif os.path.isdir(real_path):
                location = "http://"
                location += host if host is not None else self.server_name
                location += path + "/"

                res.send_move_permanently_response(self.sock, location)
                return

            with open(self.document_root + path, "rb") as fp:
                res.send_ok_response(self.sock, ext, fp)
