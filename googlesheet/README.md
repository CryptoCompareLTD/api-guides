# How to use the CryptoCompare API in Google Sheets

Official documentation [here](https://min-api.cryptocompare.com/documentation).

## Generate an API key
[Read this guide to generate an API key](https://www.cryptocompare.com/coins/guides/how-to-use-our-api/).

## Create custom function to get data into Google Sheets using Google Apps Script
[Here is a tutorial on how to use Google Apps Script](https://www.benlcollins.com/apps-script/beginner-apis/)

### Get price data
[See example Google sheet.](https://docs.google.com/spreadsheets/d/1FgrLAZqVtYAa0-9nk4q2hYE3bIuxxQ7MdRmazrT1-tU/edit?usp=sharing)
Paste the following code snippet into your script editor in Google Sheets.

```
function ccPrice(options) {
  var params = [];
  for (i in options){
    params.push(options[i][0] + "=" + options[i][1]);
  }
  var url = "https://min-api.cryptocompare.com/data/price?" + params.join("&");
  Logger.log(url);
 
  var response = UrlFetchApp.fetch(url);
  Logger.log(response.getContentText());
  
  var data = response.getContentText();
  var json = JSON.parse(data);
  var res = []
  for (key in json) {
    res.push([key, json[key]]);
  }
  return res;
}
```
You can now call ccPrice function in your sheet passing in the parameters necessary as in the example.

### Get history data
[See example Google sheet.](https://docs.google.com/spreadsheets/d/1FgrLAZqVtYAa0-9nk4q2hYE3bIuxxQ7MdRmazrT1-tU/edit?usp=sharing)
Paste the following code snippet into your script editor in Google Sheets.

```
function ccHistory(options) {
  Logger.log(options);
  var params = [];
  for (i in options){
    params.push(options[i][0] + "=" + options[i][1]);
  }
  //var url = "https://min-api.cryptocompare.com/data/histoday?" + params.join("&");
  var url = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=10&api_key=5d9f5ed136aedef7104a12f474e28453d413d884f54169441aaa80751c3b9ee5"
  Logger.log(url);
 
  var response = UrlFetchApp.fetch(url);
  Logger.log(response.getContentText());
  
  var data = response.getContentText();
  var response = JSON.parse(data);
  if (response.Response == "Error") {
    return "API Error";
  }
  var json = response.Data;
  var res = [];
  for (i in json) {
    if (i == 0) {
      var row = [];
      for (key in json[i]) {
        row.push(key);
      }
      res.push(row);
    }
    var row = [];
    for (key in json[i]) {
        row.push(json[i][key]);
    }
    res.push(row);
  }
  return res;
}
```
