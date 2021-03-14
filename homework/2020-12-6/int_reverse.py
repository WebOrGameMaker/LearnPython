import doctest
def int_reverse(num):
    """
    >>> int_reverse(987654321)
    123456789
    """
    d = 0
    while num > 0:
        num, last_digit = divmod(num, 10) # (12345678, 9)
        d = d * 10 + last_digit
    return d

if __name__ == '__main__':
    doctest.testmod(verbose=True)
