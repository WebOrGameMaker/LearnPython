def is_repdigit(num):
    """
    >>> is_repdigit(66)
    True
    >>> is_repdigit(12)
    False
    >>> is_repdigit(0)
    True
    >>> is_repdigit(-11)
    False
    >>> 
    """
    if num < 0:
        return False
    str_num = str(num)
    for i in range(len(str_num)):
        if str_num[i] != str_num[i-1]:
            return False
    return True
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)