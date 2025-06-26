import time
from datetime import datetime, date
import requests

# Discord webhook URL
webhook_url = 'discord webhook'

# Message to send
msgdata = {
    "content": "https://tenor.com/view/mad-bunny-small-gif-mad-bunny-stomp-gif-2384666291416600712"
}

# Track the last day the message was sent
last_sent_day = None

print("Bunny time checker started. Waiting for 6:00 AM...")

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    today = date.today()

    # Check if it's 6:00 AM and check if we have sent one alr
    if current_hour == 6 and current_minute == 0 and last_sent_day != today:
        response = requests.post(webhook_url, json=msgdata)
        print(f"[{now}] Sent message with status code: {response.status_code}")
        print("It's 6AM — BUNNY TIME!")
        last_sent_day = today

        # Sleep a bit longer to avoid sending multiple times in the same minute
        time.sleep(60)
    else:
        # Sleep for 30 seconds between checks (lightweight, for memory issues and so it does not boom my pc)
        time.sleep(30)

