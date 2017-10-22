import utility as utl


def send_ok_response_header(output, content_type):

    utl.write_line(output, "HTTP/1.1 200 OK")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Henacat/0.1")
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + content_type)
    utl.write_line(output, "")


def send_ok_response(output, fp, ext):

    utl.write_line(output, "HTTP/1.1 200 OK")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Henacat/0.1")
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + utl.get_content_type(ext))
    utl.write_line(output, "")

    output.send(fp.read())


def send_move_permanently_response(output, location):

    utl.write_line(output, "HTTP/1.1 301 Moved Permanently")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Henacat/0.1")
    utl.write_line(output, "Location: " + location)
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "")


def send_found_response(output, location):

    utl.write_line(output, "HTTP/1.1 302 Found")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Henacat/0.1")
    utl.write_line(output, "Location: " + location)
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + utl.get_content_type("html"))
    utl.write_line(output, "")


def send_not_found_response(output, error_document_root):

    utl.write_line(output, "HTTP/1.1 404 Not Found")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Henacat/0.1")
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + utl.get_content_type("html"))
    utl.write_line(output, "")

    with open(error_document_root + "/404.html", "rb") as fp:
        output.send(fp.read())
