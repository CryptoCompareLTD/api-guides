# How to use the CryptoCompare API with frontend javascript

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Get data into browser
There are many modules that you can use to call an API, here we are using [axios](https://www.npmjs.com/package/axios).
Add the following cdn to your frontend code:
```
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

### Send request with API key in header
```
var getFullURL = function(url, options){
    const params = [];
    for (let key in options) {
        params.push(`${key}=${options[key]}`);
    }
    return url + '?' + params.join("&");
}

var apiKey = "SET-YOUR-API-KEY";

var baseUrl = "https://min-api.cryptocompare.com/data/price"

var options = {
    fsym: "BTC",
    tsyms: "USD"
};

var headers = {
   "Authorization": "Apikey " + apiKey 
};

var fullURL = getFullURL(baseURL, options);

axios.get(fullURL, {headers: headers})
  .then(function(response) {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });

```

### Send request with API key in payload
```
var getFullURL = function(url, options){
    const params = [];
    for (let key in options) {
        params.push(`${key}=${options[key]}`);
    }
    return url + '?' + params.join("&");
}

var apiKey = "SET-YOUR-API-KEY";

var baseUrl = "https://min-api.cryptocompare.com/data/price"

var options = {
    api_key: apiKey;
    fsym: "BTC",
    tsyms: "USD"
};

var fullURL = getFullURL(baseURL, options);

axios.get(fullURL)
  .then(function(response) {
    console.log(response.data);
    console.log(response.status);
    console.log(response.statusText);
    console.log(response.headers);
    console.log(response.config);
  });
  
```

