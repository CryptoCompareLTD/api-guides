package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func getPriceMultiFull(fsyms, tsyms, apiKey string) error {

	url := apiEndpoint + "data/pricemultifull?fsyms=" + fsyms + "&tsyms=" + tsyms + "&apiKey=" + apiKey

	resp, err := http.Get(url)
	if err != nil {
		return fmt.Errorf("getPriceMultiFull, querying url, %s", err)
	}

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("getPriceMultiFull, reading body %s", err)
	}

	var respObj interface{}
	if err := json.Unmarshal(body, &respObj); err != nil {
		return fmt.Errorf("getPriceMultiFull, unmarshalling response, %s", err)
	}

	fmt.Println(respObj)

	return nil
}
