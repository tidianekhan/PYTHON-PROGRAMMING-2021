import math

hourly_wages = float(input("Enter hourly wages:"))

hours_worked = float(input("Enter numbers of hours worked:"))

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


hours_worked = round_half_up(hours_worked, 0)

total_cost = hourly_wages * hours_worked + 16

total_cost = "{:.2f}".format(total_cost)

print("The total cost of the repair is " + total_cost + " euros.")

