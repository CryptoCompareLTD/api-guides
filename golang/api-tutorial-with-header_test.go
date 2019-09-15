package main

import "testing"

func TestGetPriceMultiFullWithHeader(t *testing.T) {
	if err := getPriceMultiFullWithHeader("BTC", "USD", ""); err != nil {
		t.Fatal(err)
	}
}
