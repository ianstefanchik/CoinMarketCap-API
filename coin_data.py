import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
parameters = {
    "symbol": "BTC",
    "convert": "USD"
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "YOUR_API_KEY",
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()
btc_data = data["data"]["BTC"]
performance = btc_data["quote"]["USD"]
print(performance)
