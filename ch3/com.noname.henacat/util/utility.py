import datetime


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
    return get_content_type_map().get(ext.lower(), "application/octet-stream")
