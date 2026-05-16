import requests
import os

# Read environment variables (will come from Secrets)
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# Fetch Bitcoin and Ethereum prices
url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
response = requests.get(url, params=params)
data = response.json()

btc = data["bitcoin"]["usd"]
eth = data["ethereum"]["usd"]

# Compose the Telegram message
message = (
    f"📊 Crypto Prices\n"
    f"━━━━━━━━━━━━━━━━━\n"
    f"₿ Bitcoin:  ${btc:,.0f}\n"
    f"Ξ Ethereum: ${eth:,.0f}\n"
    f"━━━━━━━━━━━━━━━━━\n"
    f"🕐 Automatic notification"
)

# Send message via Telegram Bot API
telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
requests.post(telegram_url, json={
    "chat_id": CHAT_ID,
    "text": message
})

print("Message sent!")
