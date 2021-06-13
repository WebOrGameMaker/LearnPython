def Factorial(n):
    """
    >>> Factorial(0)
    1
    >>> Factorial(1)
    1
    >>> Factorial(5)
    120
    """
    if n > 1:
        return n * Factorial(n-1)
    return 1

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
