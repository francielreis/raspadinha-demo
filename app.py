from flask import Flask
import random
import os

app = Flask(__name__)

PREMIOS = [
    ("R$ 0", 60),
    ("R$ 2", 18),
    ("R$ 5", 12),
    ("R$ 10", 7),
    ("R$ 20", 2),
    ("R$ 50", 1),
]

def sorteio_premio():
    rotulos = [p[0] for p in PREMIOS]
    pesos = [p[1] for p in PREMIOS]
    return random.choices(rotulos, weights=pesos)[0]

@app.route("/")
def home():
    return "Sistema de raspadinha online 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
