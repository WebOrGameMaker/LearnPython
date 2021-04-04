def monotonic(nums):
    """
    >>> monotonic([1,2,2,3])
    True
    >>> monotonic([6,5,4,4])
    True
    >>> monotonic([1,3,2])
    False
    >>> monotonic([1,2,4,5])
    True
    >>> monotonic([1,1,1])
    True
    """
    monotonicity = 0 # 1 is greater than, 2 is smaller than (strings burn your cpu faster)
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            if monotonicity == 0:
                monotonicity = 1
            elif monotonicity == 2:
                return False

        if nums[i] < nums[i - 1]:
            if monotonicity == 0:
                monotonicity = 2
            elif monotonicity == 1:
                return False

    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
