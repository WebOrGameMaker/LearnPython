def adds_n(n):
    """
    >>> adds_n(10)(5)
    15
    """
    return lambda x : x + n

def adds_n_2(x):
    """
    >>> adds_n_2(23123)(1231234)
    1254357
    """
    return lambda n : n + x

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)