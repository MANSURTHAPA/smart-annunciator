import ntplib
from datetime import datetime
import time

def sync_time():
    while True:
        try:
            client = ntplib.NTPClient()
            response = client.request("pool.ntp.org")
            current_time = datetime.fromtimestamp(response.tx_time)
            print("NTP Synced:", current_time)
        except Exception as e:
            print("NTP Sync Failed:", e)

        time.sleep(300)  # sync every 5 minutes