def is_prime(n):
    """Returns a boolean indicating whether m is a prime numbers"""
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        else:
            return True


def primes(n):
    """Returns a list of all primes less than n"""
    return [i for i in range(2, n) if is_prime(i)]
