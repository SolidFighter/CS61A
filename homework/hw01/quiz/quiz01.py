def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    return a * b // gcd(a, b)

def gcd(a, b):
    """Return the greatest common divisor

    >>> gcd(2, 4)
    2
    >>> gcd(4, 2)
    2
    >>> gcd(12, 9)
    3
    >>> gcd(12, 6)
    6
    """
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    digit_set = set()
    while n != 0:
        digit_set.add(n % 10)
        n = n // 10
    return len(digit_set)