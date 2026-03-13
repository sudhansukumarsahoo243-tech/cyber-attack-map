from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/attacks")
def attacks():
    return {
        "data": [
            {"ipAddress": "8.8.8.8"},
            {"ipAddress": "1.1.1.1"},
            {"ipAddress": "185.143.223.12"},
            {"ipAddress": "45.33.32.156"}
        ]
    }

if __name__ == "__main__":
    app.run()