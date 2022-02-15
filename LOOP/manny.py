price = 0

while price < 50:
    price = int(input("Please enter the amount you wish to donate to charity:"))



print("Thank you for your donation of " + str("{:.2f}".format(price)) + " euro.")
