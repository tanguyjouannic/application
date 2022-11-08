from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "0.0.0.0"
PORT = 80

class OurServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open('/app/www/index.html', 'r') as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))

server = HTTPServer((HOST, PORT), OurServer)
print("server running")
server.serve_forever()
server.server_close()
print("server closed")
