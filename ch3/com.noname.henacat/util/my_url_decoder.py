import urllib.parse


def decode(src: str, in_encoding: str):
    return urllib.parse.unquote(src, encoding=in_encoding)
