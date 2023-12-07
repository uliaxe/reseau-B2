from http.server import BaseHTTPRequestHandler, HTTPServer

class ServHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        # Chemin du fichier demandé par le client
        requested_file = self.path[1:]  # Enlève le '/' initial
        file_path = f'htdocs/{requested_file}'

        try:
            # Ouvre le fichier demandé
            with open(file_path, 'r') as file:
                html_content = file.read()

            # Envoie la réponse HTTP avec le contenu du fichier
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode())
        except FileNotFoundError:
            # Envoie une réponse 404 si le fichier n'est pas trouvé
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