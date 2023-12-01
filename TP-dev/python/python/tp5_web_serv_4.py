from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

# Configuration des logs
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServHTTP(BaseHTTPRequestHandler):
    def get (self):
        # En-têtes de réponse standard
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Contenu de la page
        html_content = "<h1>Hello, je suis un serveur HTTP</h1>"
        self.wfile.write(html_content.encode())

        # Enregistrement de la requête dans les logs
        logging.info(f"GET request for {self.path} from {self.client_address[0]}")

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
