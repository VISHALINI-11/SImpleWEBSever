"""
Simple Web Server
Serves an HTML page listing the TCP/IP Protocol Suite.
Runs on 127.0.0.1:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

HOST = "127.0.0.1"
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Serving on http://{HOST}:{PORT}  (Press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()