import requests

url = "https://pro-api.coinmarketcap.com/v1/fiat/map"
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "YOUR_API_KEY",
}

response = requests.get(url, headers=headers)
data = response.json()
print(data)
