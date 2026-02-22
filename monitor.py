import requests
import time
from display import window, load_config

def check_connection():
    try:
        requests.get("https://google.com", timeout=5)
        return True
    except:
        return False

def monitor_connection():
    while True:
        if not check_connection():
            print("Connection lost — refreshing display")
            if window:
                config = load_config()
                window.load_url(config["display_url"])
        time.sleep(10)