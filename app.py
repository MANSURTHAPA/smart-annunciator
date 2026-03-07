from flask import Flask, render_template, request, redirect, session
import sqlite3
import json
import os

app = Flask(__name__)
app.secret_key = "super_secret_annunciator_key_12345"

DB = "database.db"
CONFIG_FILE = "config.json"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Create default admin user (only if not exists)
    c.execute("SELECT * FROM users WHERE username = 'admin'")
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  ("admin", "admin123"))

    conn.commit()
    conn.close()

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

def is_logged_in():
    return session.get("logged_in")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["logged_in"] = True
            return redirect("/")
        else:
            return "Invalid credentials"

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/login")

@app.route("/", methods=["GET", "POST"])
def dashboard():
    if not is_logged_in():
        return redirect("/login")

    config = load_config()

    if request.method == "POST":
        config["display_url"] = request.form["url"]
        save_config(config)
        return redirect("/")

    return render_template("dashboard.html", config=config)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)