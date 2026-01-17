from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

PRIZES = [
    ("R$ 0", 60),
    ("R$ 2", 18),
    ("R$ 5", 12),
    ("R$ 10", 7),
    ("R$ 20", 2),
    ("R$ 50", 1),
]

def draw_prize():
    labels = [p[0] for p in PRIZES]
    weights = [p[1] for p in PRIZES]
    return random.choices(labels, weights=weights, k=1)[0]

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/raspar", methods=["POST"])
def raspar():
    premio = draw_prize()
    return redirect(url_for("resultado", premio=premio))

@app.route("/resultado")
def resultado():
    premio = request.args.get("premio", "R$ 0")
    return render_template("resultado.html", premio=premio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
