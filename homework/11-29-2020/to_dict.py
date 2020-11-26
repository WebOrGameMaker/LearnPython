def to_dict(chr_lst):
    """
    >>> to_dict(["a", "b", "c"])
    [{'a': 97}, {'b': 98}, {'c': 99}]
    >>> to_dict(["^"])
    [{'^': 94}]
    >>> to_dict([])
    []
    """
    d = [] * len(chr_lst)
    for i in range(len(chr_lst)):
        d.append({chr_lst[i]: ord(chr_lst[i])})
    return d

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
