from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_KEY = "ff3256c3294307966e182d60b39f4398db746b3cc0da659897a5066f3a3b0428d2ca6fdacc48b493"

# Get malicious IP list
def get_attacks():

    url = "https://api.abuseipdb.com/api/v2/blacklist"

    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }

    params = {
        "confidenceMinimum": 90
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/attacks")
def attacks():

    data = get_attacks()

    return jsonify(data)

if __name__ == "__main__":
    app.run()