import requests

def getUrlToJSON(url, payload):
    return requests.get(url, params=payload).json()
    
apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "apiKey": apiKey,
    "fsym": "BTC",
    "tsyms": "USD"
}

result = getUrlToJSON(url, payload)
print(result)
"""
Result: 
{u'USD': 4069.35}
"""

