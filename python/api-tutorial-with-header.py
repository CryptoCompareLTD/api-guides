import requests

apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": "Apikey " + apiKey
}

result = requests.get(url, headers=headers, params=payload).json()

print(result)
"""
Result: 
{u'USD': 4069.35}
"""

