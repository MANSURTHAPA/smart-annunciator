import webview
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def start_display():
    config = load_config()
    url = config["display_url"]

    window = webview.create_window(
        "Annunciator Display",
        url,
        fullscreen=True
    )
    webview.start()