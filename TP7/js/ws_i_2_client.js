// Établir une connexion WebSocket avec le serveur
const socket = new WebSocket('ws://localhost:13337'); // Remplacez l'adresse IP et le port appropriés

// Exécuté lorsque la connexion est ouverte
socket.addEventListener('open', (event) => {
    console.log('Connexion établie avec le serveur WebSocket');
});

// Exécuté lorsque le serveur envoie un message
socket.addEventListener('message', (event) => {
    // Afficher la réponse du serveur dans la console (à des fins de débogage)
    console.log(`Client a reçu : ${event.data}`);

    // Afficher la réponse du serveur dans une alerte (ou autre chose selon vos besoins)
    alert(`Client a reçu : ${event.data}`);
});

// Exécuté en cas d'erreur de connexion
socket.addEventListener('error', (event) => {
    console.error('Erreur de connexion WebSocket :', event);
});

// Exécuté lorsque la connexion est fermée
socket.addEventListener('close', (event) => {
    console.log('Connexion WebSocket fermée');
});

// Fonction pour envoyer une chaîne au serveur
function sendMessage() {
    // Saisie utilisateur
    const userMessage = prompt('Saisissez une chaîne :');

    // Envoyer la chaîne au serveur si elle n'est pas vide
    if (userMessage) {
        socket.send(userMessage);
    }
}

// Appeler la fonction lorsque la page est chargée (facultatif)
document.addEventListener('DOMContentLoaded', (event) => {
    sendMessage();
});
