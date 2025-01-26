import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
parameters = {
    "symbol": "BTC,ETH",
    "convert": "USD"
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "YOUR_API_KEY",
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()
print(data)
