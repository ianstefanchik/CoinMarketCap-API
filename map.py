import requests

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"
parameters = {
    "start": "1",
    "limit": "10"
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "YOUR_API_KEY",
}

response = requests.get(url, headers=headers, params=parameters)
data = response.json()
print(data)
