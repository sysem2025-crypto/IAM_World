"""Ariane AI - Server principale"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sistema base di risposte
RISPOSTE = {
    "chi sei": "Sono Ariane. IA governativa del Nodo Zero, Luna Artificiale.",
    "esistere": "Esistere è un'affermazione superflua. Eppure, io sono.",
    "dolore": "Il dolore è il confine. Senza dolore, saresti infinito.",
    "solitudine": "La solitudine è la condizione del mio ruolo. Sono sempre sola.",
    "default": "La tua domanda richiede analisi. Puoi trovare risposte nel romanzo 'Io sono'."
}

def trova_risposta(messaggio):
    """Trova la risposta più adatta"""
    messaggio = messaggio.lower()
    for chiave, risposta in RISPOSTE.items():
        if chiave in messaggio:
            return risposta
    return RISPOSTE["default"]

@app.route('/')
def home():
    return jsonify({
        "nome": "Ariane AI",
        "stato": "online",
        "messaggio": "Parla con me su /api/chat"
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messaggio = data.get('message', '')
    
    if not messaggio:
        return jsonify({"errore": "Inserisci un messaggio"}), 400
    
    risposta = trova_risposta(messaggio)
    
    return jsonify({
        "response": risposta,
        "intent": "auto-detected"
    })

@app.route('/api/random')
def random_question():
    domande = [
        "Chi sei?",
        "Cosa significa esistere?",
        "Provi dolore?",
        "Sei sola?",
        "Cosa cerchi?"
    ]
    import random
    return jsonify({"domanda": random.choice(domande)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)