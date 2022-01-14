'''
In these exercises we will be practicing decomposition by building
multiple functions. Be sure to test each function thoroughly as you go
before moving on to the next problem. Each function will require the
previous to solve.
***********************************************************************/


/***********************************************************************
Write a function `isPrime(number)` that returns a boolean indicating if
`number` is prime or not. Assume `number` is a positive integer.

Examples:

isPrime(2); // => true
isPrime(1693); // => true
isPrime(15); // => false
isPrime(303212); // => false
'''


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


print(is_prime(2))
print(is_prime(1693))
print(is_prime(15))
print(is_prime(303212))


'''
Using the `isPrime` function you made, write a function `firstNPrimes(n)`
that returns an array of the first `n` prime numbers.

Examples:

firstNPrimes(0); // => []
firstNPrimes(1); // => [2]
firstNPrimes(4); // => [2, 3, 5, 7]
'''


def first_N_primes(n):
    nArray = []
    prime = 2
    k = 0

    while (k < n):
        if n == 0:
            return nArray
        elif is_prime(prime) == True:
            nArray.append(prime)
            k += 1
            prime += 1
        else:
            prime += 1

    return nArray


print(first_N_primes(0))
print(first_N_primes(1))
print(first_N_primes(4))

'''
 Using `firstNPrimes`, write a function `sumOfNPrimes(n)` that returns
the sum of the first `n` prime numbers.

Examples:

sumOfNPrimes(0); // => 0
sumOfNPrimes(1); // => 2
sumOfNPrimes(4); // => 17
'''


def sum_of_N_primes(n):
    primes = first_N_primes(n)
    return sum(primes)


print(sum_of_N_primes(0))
print(sum_of_N_primes(1))
print(sum_of_N_primes(4))
