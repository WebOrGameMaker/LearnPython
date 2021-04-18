def list_flipper(lst):
    """
    >>> list_flipper([1, 2, 3, 4])
    [[1], [2], [3], [4]]
    >>> list_flipper([[1], [2], [3], [4]])
    [1, 2, 3, 4]
    >>> list_flipper([])
    []
    """
    flipped = []
    if len(lst) == 0:
        return flipped
    
    elif isinstance(lst[0], list):
        for i in range(len(lst)):
            flipped.append((lst[i])[0])

    else:
        for i in range(len(lst)):
            flipped.append([(lst[i])])

    return flipped

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
