def find(lst):
    """
    >>> find(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    ['Monday', 'Friday', 'Sunday']
    """
    output = []
    for i in range(len(lst)):
        if len(lst[i]) == 6:
            output.append(lst[i])
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
