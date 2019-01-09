import requests

def getUrlToJSON(url):
    return requests.get(url).json()
    
def generateURL(endpoint, options):
    params = []
    for key in options:
        params.append("{}={}".format(key, options[key]))
    return endpoint + "?" + "&".join(params)
    
apiKey = "SET-YOUR-API-KEY-HERE"

endpoint = "https://min-api.cryptocompare.com/data/price"

options = {
    "apiKey": apiKey,
    "fsym": "BTC",
    "tsyms": "USD"
}

url = generateURL(endpoint, options)
result = getUrlToJSON(url)
print(result)

