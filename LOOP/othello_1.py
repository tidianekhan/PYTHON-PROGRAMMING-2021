white_pieces = float(input("Enter the number of white pieces on the board:"))
black_pieces = float(input("Enter the number of black pieces on the board:"))

total_number_of_pieces = white_pieces + black_pieces

black_percent = (black_pieces/64) * 100
black_percent_two = (black_pieces/total_number_of_pieces) * 100

round_1 = '{:.2f}'.format(round(black_percent, 2))
round_2 = '{:.2f}'.format(round(black_percent_two, 2))


print("The percentage of black pieces on the board is: " + str(round_1) + "%")
print("The percentage of black pieces of all the pieces on the board is: " + str(round_2) + "%")