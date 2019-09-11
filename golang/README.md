# How to use the CryptoCompare API with golang

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Get data from API 
There are many modules to do an http request, in this example we use the request npm module.

### Send API key in request header
You can choose to send your authentication in the request header as in [api-tutorial-with-header.go](https://github.com/CryptoCompareLTD/api-guides/blob/master/golang/api-tutorial-with-header.go) or in the request parameters as in [api-tutorial.go](https://github.com/CryptoCompareLTD/api-guides/blob/master/golang/api-tutorial.go).
