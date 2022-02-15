import string
def palindrome_2():
    letter = str(input("Please enter a letter:"))
    alphabet = ""
    for i in range(97, 97 + 26):
        alphabet += chr(i)
    palindrome = alphabet + alphabet[-2::-1]
    n = palindrome.find(letter)
    string = palindrome[:n+1]
    print(string + string[-2::-1])


palindrome_2()