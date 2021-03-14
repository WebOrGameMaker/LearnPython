def distinct_nums(nums):
    """
    >>> distinct_nums([1, 2, 3, 4, 5, 6, 7, 8, 9])
    False
    >>> distinct_nums([8, 1, 4, 7, 9, 6, 5, 1, 3])
    True
    """
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1:
            return True
    return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
