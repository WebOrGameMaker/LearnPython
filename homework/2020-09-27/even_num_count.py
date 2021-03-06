def count(lst):
    """
    >>> count([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1])
    9
    """
    o = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            o += 1
    return o


def lambda_func(lst2):
    """
    >>> count([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1])
    9
    """
    return len(list(filter(lambda x : x % 2 == 0, lst2)))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)