from http.server import HTTPServer, SimpleHTTPRequestHandler


HOST, PORT = "localhost", 8888


class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        print("Command: ")
        print(self.command)
        print("Path: ")
        print(self.path)
        print("Request headers: ")
        print(self.headers)

        html_content = "<html><body><h1>Hello World ...!</h1></body></html>"
        self.wfile.write(html_content.encode())


if __name__ == "__main__":
    simple_server = HTTPServer((HOST, PORT), SimpleServer)
    print("Starting server ...\n")

    try:
        simple_server.serve_forever()
    except KeyboardInterrupt:
        pass

    simple_server.server_close()
    print("Server shutting down ...")
