const request = require('request');

const apiKey = "SET-YOUR-API-KEY-HERE";

function getFullURL(url, options){
    const params = []
    for (let key in options) {
        params.push(`${key}=${options[key]}`)
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
