import http.client

def simple_http_client():
    # Adresse du serveur
    server_address = "10.1.2.15"
    port = 13337

    # Création d'une connexion au serveur
    connection = http.client.HTTPConnection(server_address, port)

    try:
        # Envoi d'une requête GET
        connection.request("GET", "/")

        # Récupération de la réponse du serveur
        response = connection.getresponse()

        # Affichage de la réponse
        print("Code de réponse:", response.status)
        print("En-têtes de réponse:")
        for header, value in response.getheaders():
            print(f"{header}: {value}")

        # Affichage du corps de la réponse
        body = response.read().decode("utf-8")
        print("\nCorps de la réponse:")
        print(body)

    finally:
        # Fermeture de la connexion
        connection.close()

if __name__ == "__main__":
    simple_http_client()
