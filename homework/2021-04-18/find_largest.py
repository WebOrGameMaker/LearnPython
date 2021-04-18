def binary_search_largest(nums, k):
    """
    >>> binary_search_largest([1,2,4], 3) 
    -1
    >>> binary_search_largest([1,2,3,3,3,3,4], 3)
    5
    >>> binary_search_largest([1,2,3,4], -1)
    -1
    >>> binary_search_largest([1,2,3,4], 5)
    -1
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > k:
            high = mid
        else:
            low = mid + 1

    if low > 0 and nums[low - 1] == k:
        return low - 1
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
