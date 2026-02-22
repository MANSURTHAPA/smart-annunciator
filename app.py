from flask import Flask, render_template, request, redirect
import json
import threading
from display import start_display
from ntp_sync import sync_time

app = Flask(__name__)

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def save_config(data):
    with open("config.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    config = load_config()

    if request.method == "POST":
        config["display_url"] = request.form["url"]
        save_config(config)
        return redirect("/")

    return render_template("dashboard.html", config=config)

if __name__ == "__main__":
    threading.Thread(target=sync_time).start()
    threading.Thread(target=start_display).start()
    app.run(port=5000)