from http.server import HTTPServer, SimpleHTTPRequestHandler


HOST, PORT = "localhost", 8888


class SimpleServer(SimpleHTTPRequestHandler):
    pass


if __name__ == "__main__":
    simple_server = HTTPServer((HOST, PORT), SimpleServer)

    simple_server.serve_forever()
    simple_server.server_close()
