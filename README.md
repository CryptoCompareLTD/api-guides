# How to use the CryptoCompare API

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Tutorials
Here you can find a few code examples written in different languages so you get quickly get started.

* [Python tutorials](https://github.com/CryptoCompareLTD/api-guides/tree/master/python)
* [Node tutorials](https://github.com/CryptoCompareLTD/api-guides/tree/master/node)
* [Javascript (frontend) tutorials](https://github.com/CryptoCompareLTD/api-guides/tree/master/javascript)
* [Google Sheets tutorials](https://github.com/CryptoCompareLTD/api-guides/tree/master/googlesheet)

## Rate limit
You get the following error message if you are out of the rate limit:
```
{
	"Response": "Error",
	"Message": "You are over your rate limit please upgrade your account!",
	"HasWarning": false,
	"Type": 99,
	"RateLimit": {
		"calls_made": {
			"second": 53,
			"minute": 915,
			"hour": 63283,
			"day": 127321,
			"month": 6720577,
			"total_calls": 29374377
		},
		"max_calls": {
			"second": 50,
			"minute": 2000,
			"hour": 100000,
			"day": 1500000,
			"month": 15000000
		}
	},
	"Data": {}
}
```
