# def esrever(n):
#     """
#     >>> esrever(334554321123322)
#     223321123455433
#     >>> esrever(334554321123211)
#     112321123455433
#     >>> esrever(1293)
#     3921
#     """
#     if n < 10:
#         return n
#     else:
#         return int(str(n % 10) + str(esrever(n//10)))


def esrever2(n, s):
    """
    >>> esrever2(12345, 0)
    54321
    >>> esrever2(12340, 0)
    4321
    """
    if n == 0:
        return s
    else:
        result = esrever2(n // 10, s * 10 + n % 10)
        return result

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
