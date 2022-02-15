def bubble_sort():
    input_string = input('Enter elements of a list separated by space ')
    print("\n")
    ex_list = input_string.split()
    for i in range(len(ex_list)):
        ex_list[i] = int(ex_list[i])
    for i in range(len(ex_list)):
        for j in range(len(ex_list) - 1):
            if ex_list[j] > ex_list[j+1]:
                ex_list[j], ex_list[j+1] = ex_list[j+1], ex_list[j]
    print(ex_list)

bubble_sort()


