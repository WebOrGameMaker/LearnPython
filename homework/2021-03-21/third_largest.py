def third_largest(nums):
    """
    >>> third_largest([2, 4, 7, 3, 10, 4, 9, 23])
    9
    >>> third_largest([1])
    -1
    """
    if len(nums) > 3:
        first = nums[0]
        second = nums[0]
        third = nums[0]
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third
    else:
        return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
