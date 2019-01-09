import requests

apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "apiKey": apiKey,
    "fsym": "BTC",
    "tsyms": "USD"
}

result = requests.get(url, params=payload).json()

print(result)
"""
Result: 
{u'USD': 4069.35}
"""

