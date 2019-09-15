package main

import "testing"

func TestGetPriceMultiFull(t *testing.T) {
	if err := getPriceMultiFull("BTC", "USD", ""); err != nil {
		t.Fatal(err)
	}
}
