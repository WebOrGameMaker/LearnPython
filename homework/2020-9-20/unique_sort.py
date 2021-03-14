def unique_sort(lst):
    """
    >>> unique_sort([1, 2, 4, 3])
    [1, 2, 3, 4]
    >>> unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2])
    [1, 2, 3, 4]
    >>> unique_sort([6, 7, 3, 2, 1])
    [1, 2, 3, 6, 7]
    """
    s = set(lst)
    lst2 = sorted(s)
    return lst2

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)