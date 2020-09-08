def return_unique(lst):
    """
    >>> return_unique([1, 9, 8, 8, 7, 6, 1, 6])
    [9, 7]
    >>> return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
    [2, 1]
    >>> return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])
    [5, 6]
    """
    output = []
    for i in range(0, len(lst), 1):
        if lst.count(lst[i]) == 1:
            output.append(lst[i])
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod()