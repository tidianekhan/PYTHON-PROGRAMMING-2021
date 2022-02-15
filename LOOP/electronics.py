import math

a = int(input("Enter the price of the first article:"))
b = int(input("Enter the price of the second article:"))
c = int(input("Enter the price of the third article:"))

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

if b <= a >= c:
    discount_article = a * 0.85
    discount = a - discount_article
    total_price = discount_article + b + c
elif a <= b >= c:
    discount_article = b * 0.85
    discount = b - discount_article
    total_price = discount_article + a + c
elif b <= c >= a:
    discount_article = c * 0.85
    discount = c - discount_article
    total_price = discount_article + b + a




print("Discount: " + str("{:.2f}".format(discount)))
print("Total: " + str("{:.2f}".format(total_price)))

