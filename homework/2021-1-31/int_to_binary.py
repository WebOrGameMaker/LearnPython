def binary_str(num):
    """
    >>> binary_str(23937495825)
    '10110010010110010010011001100010001'
    >>> binary_str(876765)
    '11010110000011011101'
    >>> binary_str(213)
    '11010101'
    """
    digits = []
    while num > 0:
        current_digit = num % 2
        digits.append(str(current_digit))
        num //= 2
    digits.reverse()
    return "".join(digits)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
