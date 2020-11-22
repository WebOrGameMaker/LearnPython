def invert2(d):
    """
    >>> invert2({ 'z': 'q', 'w': 'f'})
    {'q': 'z', 'f': 'w'}
    >>> invert2({ 'a': 1, 'b': 2, 'c': 3})
    {1: 'a', 2: 'b', 3: 'c'}
    >>> invert2({'zebra': 'koala', 'horse': 'camel'})
    {'koala': 'zebra', 'camel': 'horse'}
    """
    d_copy = d.copy()
    d.clear()
    for key, value in d_copy.items():
        d[value] = key
    return d


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
