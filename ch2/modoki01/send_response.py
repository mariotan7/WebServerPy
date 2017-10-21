import utility as utl


def send_ok_response(output, ext, fp):

    utl.write_line(output, "HTTP/1.1 200 OK")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Modoki/0.2")
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + utl.get_content_type(ext))
    utl.write_line(output, "")

    output.send(fp.read())


def send_move_permanently_response(output, location):

    utl.write_line(output, "HTTP/1.1 301 Moved Permanently")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Modoki/0.2")
    utl.write_line(output, "Location: " + location)
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "")


def send_not_found_response(output, error_document_root):

    utl.write_line(output, "HTTP/1.1 404 Not Found")
    utl.write_line(output, "Date: " + utl.get_date_string_utc())
    utl.write_line(output, "Server: Modoki/0.2")
    utl.write_line(output, "Connection: close")
    utl.write_line(output, "Content-type: " + utl.get_content_type("html"))
    utl.write_line(output, "")

    with open(error_document_root + "/404.html", "rb") as fp:
        output.send(fp.read())
