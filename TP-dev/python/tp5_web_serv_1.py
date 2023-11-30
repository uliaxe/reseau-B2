from http.server import BaseHTTPRequestHandler, HTTPServer

class ServHTTP(BaseHTTPRequestHandler):
    def get(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, je suis un vrai serveur HTTP !</h1>')
        
    def run():
        port = 8080
        serv_address = ('', port)
        httpd = HTTPServer(serv_address, ServHTTP)
        print('Serveur web démarré sur le port {port}')
        httpd.serve_forever()

    if __name__ == '__main__':
        run()
    