input_string = input('Enter elements of a list separated by space ')
print("\n")
t_list = input_string.split()
for i in range(len(t_list)):
    t_list[i] = int(t_list[i])

t_list.sort()
print(t_list[1])
