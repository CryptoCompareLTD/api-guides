# How to use the CryptoCompare API with python

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Get data from API 
There are many python libraries to do an http request, in this example we use the requests library.

### Send API key in request header
You can choose to send your authentication in the request header as in [this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/python/api-tutorial-with-header.py).

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

### Send API key in request payload
You can send the API key as a request payload as in [this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/python/api-tutorial.py).

```
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
```

### Load historical data into pandas dataframe
Pandas is a popular tool among data scientists, [in this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/python/api-tutorial-pandas.py) we show an example how to load historical data into a dataframe.

```
import requests
import pandas as pd

apiKey = "SET-YOUR-API-KEY-HERE"

url = "https://min-api.cryptocompare.com/data/histoday"

payload = {
    "apiKey": apiKey,
    "fsym": "BTC",
    "tsym": "USD",
    "limit": 100
}

result = requests.get(url, params=payload).json()

df = pd.DataFrame(result['Data'])

print(df.head())

"""
     close     high      low     open        time  volumefrom      volumeto
0  6594.98  6662.60  6510.54  6623.82  1538352000    38926.98  2.569599e+08
1  6525.47  6618.95  6478.04  6594.98  1538438400    40624.20  2.671663e+08
2  6492.26  6537.07  6428.98  6525.46  1538524800    47186.00  3.063853e+08
3  6579.79  6622.32  6486.86  6492.61  1538611200    42142.96  2.776140e+08
4  6632.87  6683.55  6546.98  6580.00  1538697600    39731.28  2.625623e+08

"""
```

