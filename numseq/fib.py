def fib(n):
    """fibonacci sequence: lists all the numbers up to nth Fibonacci number"""
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n
