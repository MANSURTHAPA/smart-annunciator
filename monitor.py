import requests
import time
import json

def check_connection():
    try:
        requests.get("https://google.com", timeout=5)
        return True
    except:
        return False

def monitor_connection(refresh_callback):
    while True:
        if not check_connection():
            print("Connection lost. Refreshing...")
            refresh_callback()
        time.sleep(10)