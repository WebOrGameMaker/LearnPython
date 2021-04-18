def binary_search_smallest(nums, k):
    """
    >>> binary_search_smallest([1,3,3,4,4,4,5,6], 0) 
    -1
    >>> binary_search_smallest([1,3,3,4,4,4,5,6], 2)
    -1
    >>> binary_search_smallest([1,3,3,4,4,4,5,6], 3)
    1
    >>> binary_search_smallest([1,3,3,4,4,4,5,6], 7)
    -1
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= k:  # k <= nums[mid]
            high = mid
        else:
            low = mid + 1

    if low < len(nums) and nums[low] == k:
        return low
    return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
