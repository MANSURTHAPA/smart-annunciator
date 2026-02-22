import webview
import json

window = None

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def start_display():
    global window
    config = load_config()

    window = webview.create_window(
        "Annunciator Display",
        config["display_url"],
        fullscreen=True
    )

    webview.start()