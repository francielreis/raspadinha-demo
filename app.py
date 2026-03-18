from flask import Flask
import random

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
    return random.choices(rotulos, weights=pesos, k=1)[0]

@app.route("/")
def home():
    return "Sistema de raspadinha online 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
