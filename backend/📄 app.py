from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8080


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()