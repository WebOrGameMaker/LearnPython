def index_finder(nums, target):
    """
    >>> index_finder([1,3,5,6], 5)
    2
    >>> index_finder([1,3,5,6], 2)
    1
    >>> index_finder([1,3,5,6], 7)
    4
    >>> index_finder([1,3,5,6], 0)
    0
    >>> index_finder([1], 0)
    0
    """
    for i in range(len(nums)):
        if target <= nums[i]:
            return i
    return len(nums)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
