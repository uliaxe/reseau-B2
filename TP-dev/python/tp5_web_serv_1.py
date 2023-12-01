from http.server import BaseHTTPRequestHandler, HTTPServer

class ServHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Received GET request")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello je suis un serveur HTTP</h1>')

def run():
    port = 13337
    serv_address = ('', port)
    print(f"Starting server on port {port}...")
    try:
        httpd = HTTPServer(serv_address, ServHTTP)
        httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    run()
