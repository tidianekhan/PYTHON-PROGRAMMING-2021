price_with_VAT = int(input("Enter the price of an article including VAT: "))

price_without_VAT = (float(price_with_VAT/1.210))

price_without_VAT = "{:.2f}".format(price_without_VAT)



print("This article will cost " + price_without_VAT + " euro without 21.00% VAT.")



