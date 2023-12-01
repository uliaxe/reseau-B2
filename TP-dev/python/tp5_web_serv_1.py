from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

class ServHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Received GET request")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello je suis un serveur HTTP</h1>')

def run(server_class=HTTPServer, handler_class=ServHTTP, port=13337):
    serv_address = ('', port)
    print(f"Starting server on port {port}...")
    try:
        httpd = server_class(serv_address, handler_class)
        httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Exécute le serveur dans un thread séparé
    server_thread = Thread(target=run)
    server_thread.start()

    # Continuez à exécuter d'autres opérations ici
    print("Le serveur est en cours d'exécution. Vous pouvez faire d'autres choses dans ce script.")

    # Attendez que le thread du serveur se termine
    server_thread.join()
