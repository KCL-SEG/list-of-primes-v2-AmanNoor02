"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    num = 1
    while len(list) < number_of_primes:
        isPrime = True
        num += 1
        if num > 1:
            for j in range(2, num):
                if (num%j) == 0:
                    isPrime = False
                    break
        if isPrime:
            list.append(num)

    return list
number_of_primes = 10
try:
    primes(number_of_primes)
    print (primes(number_of_primes))
except ValueError:
    print ("Sorry, this is an invalid input")
