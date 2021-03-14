def missing_num(nums):
    """
    >>> missing_num([0, 9, 1, 8, 2, 6, 3, 5, 4])
    7
    >>> missing_num([9, 5, 0, 1, 8, 4, 7, 6, 3])
    2
    """
    i = 0 # keeps track of which number you're on and it is added to the total
    total = 0
    while i < len(nums) + 1: # len(nums) + 1 is the length of the list with every number
        total += i
        i += 1
    return total - sum(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
