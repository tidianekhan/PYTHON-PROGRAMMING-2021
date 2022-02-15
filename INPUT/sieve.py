l = [True for i in range(0, 20)]

def cross_out_multiples(is_prime,n):
    is_prime[0] = is_prime[1] = True
    for x in is_prime[4:]:
        if is_prime:
            for i in range(n, len(is_prime), n):
                is_prime[i] = False
            return is_prime





def sieve(n):
    prime_numbers = []
    for num in range(2,n):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            prime_numbers.append(num)

    return prime_numbers


print(sieve(20))




