def sum_digits(num):
    """
    >>> sum_digits(0)
    0
    >>> sum_digits(12345)
    15
    """
    if num == 0:
        return 0
    return num % 10 + sum_digits(num // 10)

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
