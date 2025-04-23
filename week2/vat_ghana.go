package main

import "fmt"

// Current VAT rate and levies in Ghana (as of my last update)
const vatRate float64 = 0.15
const nhilRate float64 = 0.025
const getFundRate float64 = 0.025
const covid19HRLRate float64 = 0.01 // Verify current application

// CalculateVATGhana calculates the Value Added Tax (VAT) in Ghana,
// considering the NHIL, GETFund Levy, and COVID-19 Health Recovery Levy.
//
// Args:
//   amount: The original price of the goods or services (float64).
//
// Returns:
//   The calculated VAT amount (float64).
func CalculateVATGhana(amount float64) float64 {
	totalWithLevies := amount * (1 + nhilRate + getFundRate + covid19HRLRate)
	vatAmount := totalWithLevies * vatRate
	return vatAmount
}

// CalculateTotalWithVATGhana calculates the total amount including VAT and all levies.
//
// Args:
//   amount: The original price of the goods or services (float64).
//
// Returns:
//   The total amount including VAT and levies (float64).
func CalculateTotalWithVATGhana(amount float64) float64 {
	vat := CalculateVATGhana(amount)
	totalWithLevies := amount * (1 + nhilRate + getFundRate + covid19HRLRate)
	return totalWithLevies + vat
}

func main() {
	price := 100.0
	vatAmount := CalculateVATGhana(price)
	totalPrice := CalculateTotalWithVATGhana(price)

	fmt.Printf("Original Price: %.2f GH₵\n", price)
	fmt.Printf("NHIL (%.1f%%): %.2f GH₵\n", nhilRate*100, price*nhilRate)
	fmt.Printf("GETFund Levy (%.1f%%): %.2f GH₵\n", getFundRate*100, price*getFundRate)
	fmt.Printf("COVID-19 HRL (%.0f%%): %.2f GH₵\n", covid19HRLRate*100, price*covid19HRLRate)
	fmt.Printf("Subtotal (Price + Levies): %.2f GH₵\n", price*(1+nhilRate+getFundRate+covid19HRLRate))
	fmt.Printf("VAT (%.0f%% of Subtotal): %.2f GH₵\n", vatRate*100, vatAmount)
	fmt.Printf("Total Price (including VAT and Levies): %.2f GH₵\n", totalPrice)
}