import string
'''def palindrome_2():
    letter = str(input("Please enter a letter:"))
    alphabet = ""
    for i in range(97, 97 + 26):
        alphabet += chr(i)
    palindrome = alphabet + alphabet[-2::-1]
    n = palindrome.find(letter)
    string = palindrome[:n+1]
    print(string + string[-2::-1])'''


def pyramid():
    letter = str(input("Please enter a letter:"))
    alphabet = ""
    for i in range(97, 97 + 26):
        alphabet += chr(i)
    palindrome = alphabet + alphabet[-2::-1]
    n = palindrome.find(letter)
    for x in range(0, n+1):
        string = palindrome[0:x+1]
        pyramid_string = string + string[-2::-1]
        pyramid_string = pyramid_string.center(40)
        print(pyramid_string)


pyramid()