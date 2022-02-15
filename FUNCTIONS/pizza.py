
def factorial(n):
    base_num = 1
    for x in range(1, n+1):
        base_num *= x
    return base_num

def choose(n, k):
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)
    return a/(b*c)



if __name__ == '__main__':
    mario_bet = int(choose(10,3))
    luigi_bet = int(choose(9,4))

    print("Mario can make " + str(mario_bet) + " pizzas.")
    print("Luigi can make " + str(luigi_bet) + " pizzas.")

    if mario_bet > luigi_bet:
        print("Mario has won the bet.")
    if luigi_bet > mario_bet:
        print("Luigi has won the bet.")

