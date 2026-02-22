import ntplib
from datetime import datetime

def sync_time():
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    current_time = datetime.fromtimestamp(response.tx_time)
    print("NTP Synced Time:", current_time)