# How to use the CryptoCompare API with python

## Generate an API key
Read this [guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/)

## Get data from API 
There are many python libraries to do an http request, in this example we use the requests library.
You can choose to send your authentication in the request header as in [this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/python/api-tutorial-with-header.py)

```
import requests

apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/price"

payload = {
    "fsym": "BTC",
    "tsyms": "USD"
}

headers = {
    "authorization": apiKey
}

result = requests.get(url, headers=headers, params=payload).json()

print(result)
"""
Result: 
{u'USD': 4069.35}
"""

```
