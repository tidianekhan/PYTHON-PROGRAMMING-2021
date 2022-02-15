
def palindrome():
    alphabet = ""
    for i in range(97, 97+26):
        alphabet += chr(i)
    print(alphabet + alphabet[-2::-1])


palindrome()