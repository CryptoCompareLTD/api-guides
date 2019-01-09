# How to use the CryptoCompare API with node

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Get data from API 
There are many modules to do an http request, in this example we use the request npm module.

### Send API key in request header
You can choose to send your authentication in the request header as in [this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/node/api-tutorial-with-header.js).

```
const request = require('request');

const apiKey = "SET-YOUR-API-KEY-HERE";

function getFullURL(url, options){
    const params = [];
    for (let key in options) {
        params.push(`${key}=${options[key]}`);
    }
    return url + '?' + params.join("&");
}

const baseURL = "https://min-api.cryptocompare.com/data/price";

const options = {
    api_key: apiKey,
    fsym: "BTC",
    tsyms: "USD"
};

const headers = {
   "Authorization": apiKey 
};

const fullURL = getFullURL(baseURL, options);

request.get({
    url: fullURL,
    headers: headers
}, function(err, res, body){
    if (err){
        console.log(err);
    } else {
        console.log(body);
    }
});
```

### Send API key in request payload
You can send the API key as a request payload as in [this tutorial](https://github.com/CryptoCompareLTD/api-guides/blob/master/node/api-tutorial.js).

```
const request = require('request');

const apiKey = "SET-YOUR-API-KEY-HERE";

function getFullURL(url, options){
    const params = [];
    for (let key in options) {
        params.push(`${key}=${options[key]}`);
    }
    return url + '?' + params.join("&");
}

const baseURL = "https://min-api.cryptocompare.com/data/price";

const options = {
    api_key: apiKey,
    fsym: "BTC",
    tsyms: "USD"
};

const fullURL = getFullURL(baseURL, options);

request.get(fullURL, function(err, res, body){
    if (err){
        console.log(err);
    } else {
        console.log(body);
    }
});
```
