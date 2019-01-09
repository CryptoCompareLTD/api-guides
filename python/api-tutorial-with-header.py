import requests

def getUrlToJSON(url, headers, payload):
    return requests.get(url, headers=headers, params=payload).json()
    
def generateURL(endpoint, options):
    params = []
    for key in options:
        params.append("{}={}".format(key, options[key]))
    return endpoint + "?" + "&".join(params)
    
apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": apiKey
}

result = getUrlToJSON(url, headers, payload)
print(result)
"""
Result: 
{u'USD': 4069.35}
"""

