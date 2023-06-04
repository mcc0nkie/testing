from Decorator import profile
from functools import lru_cache

@profile
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@profile
def cached_factorial(n):
    return factorial(n)

cached_factorial(100000)

