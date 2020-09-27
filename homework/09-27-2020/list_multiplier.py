def multiply(lst):
    """
    >>> multiply([4, 5])
    [[4, 4], [5, 5]]

    >>> multiply(['*', '%', '$'])
    [['*', '*', '*'], ['%', '%', '%'], ['$', '$', '$']]

    >>> multiply(['A', 'B', 'C', 'D', 'E'])
    [['A', 'A', 'A', 'A', 'A'], ['B', 'B', 'B', 'B', 'B'], ['C', 'C', 'C', 'C', 'C'], ['D', 'D', 'D', 'D', 'D'], ['E', 'E', 'E', 'E', 'E']]
    """
    o = []
    for i in range(len(lst)):
        curr_value = lst[i]
        temp_list = [curr_value] * len(lst)
        o.append(temp_list)
    return o

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)