import requests
import time
import random
from evpn import ExpressVpnApi  # Assumes evpn works properly

# Your target URL and params
url = "https://www.klook.com/activity/143928-dunia-fantasi-ancol/"
params = {
    'spm': 'Home.SearchSuggest_LIST',
    'clickId': '049c826980',
}

# List of fake User-Agents for randomization
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/115.0",
]

try:
    for i in range(10):  # You can set this to 1000 later
        with ExpressVpnApi() as api:
            # Step 1: Connect to a random VPN location
            locations = api.locations
            loc = random.choice(locations)
            try:
                api.connect(loc["id"])
                print(f"{i+1}: 🌐 Connected to {loc['name']}")
                time.sleep(10)  # Allow VPN to fully connect
            except Exception as e:
                print(f"{i+1}: ❌ VPN connection failed - {e}")
                continue

            # Step 2: Prepare headers and send request
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Referer": "https://www.google.com/",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
            }

            try:
                response = requests.get(url, headers=headers, params=params, timeout=10)
                if response.status_code == 200 and "Dunia Fantasi" in response.text:
                    print(f"{i+1}: ✅ Success! Response received.")
                else:
                    print(f"{i+1}: ❌ Blocked. Status Code: {response.status_code}")
            except Exception as e:
                print(f"{i+1}: ❌ Request error - {e}")

            # Step 3: Disconnect VPN
            try:
                api.disconnect()
                print(f"{i+1}: 🔌 VPN disconnected.\n")
            except Exception as e:
                print(f"{i+1}: ⚠️ VPN disconnect failed - {e}")

            time.sleep(5)  # Pause before next iteration

except KeyboardInterrupt:
    print("⛔ Stopped by user.")
