from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        # En-tête de réponse standard
        self.send_response(200)

        # Spécifiez le type MIME du fichier que vous envoyez (exemple : image/jpeg)
        content_type = "image/jpeg"  # Changez cela en fonction du type de fichier que vous souhaitez prendre en charge
        self.send_header('Content-type', content_type)
        self.end_headers()

        # Chemin du fichier à envoyer (exemple : image.jpg)
        file_path = f'htdocs/{self.path[1:]}'  # Supprimez le '/' initial du chemin

        try:
            with open(file_path, 'rb') as file:
                # Envoyer le fichier morceau par morceau (chunks)
                chunk_size = 8192  # Taille de chaque morceau (en octets)
                chunk = file.read(chunk_size)
                while chunk:
                    self.wfile.write(chunk)
                    chunk = file.read(chunk_size)

            # Enregistrement de la requête dans les logs
            logging.info(f"GET request for {self.path} from {self.client_address[0]}")

        except FileNotFoundError:
            # Envoyer une réponse 404 si le fichier n'est pas trouvé
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404 Not Found</h1>')

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
