import cProfile
import pstats
from numseq.prime import *
from numseq.geo import *
from numseq.fib import fib


def profile(func):
    def profile_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        pr_func = func(*args, **kwargs)
        pr.disable()
        ps = pstats.Stats(pr).sort_stats('cumulative')
        ps.print_stats()
        return pr_func
    return profile_function


@profile
def test_modules():
    print("Fibonacci")
    for i in range(10):
        print("{}: {}".format(i, fib(i)))

    print("Geometric numbers (square, triangle, cube)")
    for i in range(10):
        print("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

    print("Primes")
    prime_list = primes(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    test_modules()
