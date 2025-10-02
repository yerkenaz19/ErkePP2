def filter_primes(numbers):
    primes = list(filter(lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))
    print(primes)

filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])