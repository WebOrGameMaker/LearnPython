def recursive_binary(nums, t, high, low):
    """
    >>> recursive_binary([], 2234, -1, 0)
    False
    >>> recursive_binary([1,2,3,3,4,5], 0, 5, 0)
    False
    >>> recursive_binary([1,2,3,3,4,5,5], 4, 6, 0)
    True
    """
    if low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == t:
            return True
        elif nums[mid] < t:
            return recursive_binary(nums, t, high, mid + 1)
        return recursive_binary(nums, t, mid - 1, low)
    return False

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
