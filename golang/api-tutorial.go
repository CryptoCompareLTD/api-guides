package main

import (
	"io/ioutil"
	"log"
	"net/http"
	"encoding/json"
	"fmt"
)

func main() {
	apiKey := ""
	url := "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&apiKey=" + apiKey

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("authorization", header)

	client := &http.Client{}

	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	responseData, err := ioutil.ReadAll(resp.Body)
    if err != nil {
        log.Fatal(err)
    }
	
	var responseObj interface{}
	interfaceErr := json.Unmarshal(responseData, &responseObj)
	if interfaceErr != nil {
        log.Fatal(err)
    }

	fmt.Println(responseObj)

}