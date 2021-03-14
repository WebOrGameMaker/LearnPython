def find_missing(lst):
    """
    >>> find_missing([5, 3, 1, 0, 4])
    2
    >>> find_missing([1, 0, 2])
    3
    >>> find_missing([2, 1, 3])
    0
    """
    i = 0
    total = 0
    while i < len(lst)+1:
        total += i
        i += 1
    return total - sum(lst)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
