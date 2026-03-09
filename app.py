from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

# Example malicious IPs
ips = [
"185.143.223.12",
"103.21.244.0",
"45.33.32.156",
"8.8.8.8"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api():

    ip = random.choice(ips)

    url = f"https://ipinfo.io/{ip}/json"
    data = requests.get(url).json()

    return jsonify(data)

if __name__ == "__main__":
    app.run()