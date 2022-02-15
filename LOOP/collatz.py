




def collatz_conjecture(i):
    list1 = [i]
    if i == 1:
        return [1]
    elif i % 2 == 0:
        list1.extend(collatz_conjecture(i // 2))
    else:
        list1.extend(collatz_conjecture(i * 3 + 1))
    return list1






def collatz_conjecture_number():
    x = int((input("Please enter a number:")))
    listToStr = ' '.join(map(str, collatz_conjecture(x)))
    print(listToStr)


collatz_conjecture_number()









