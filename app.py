
from flask import Flask, render_template, jsonify
import json
from pathlib import Path

app = Flask(__name__)

BASE = Path(__file__).resolve().parent

with open(BASE / "data.json", "r", encoding="utf-8") as f:
    payload = json.load(f)

@app.route("/")
def index():
    return render_template(
        "index.html",
        stats=payload["stats"],
        records=payload["records"]
    )

@app.route("/api/summary")
def summary():
    return jsonify(payload["stats"])

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
