def selection_sort(nums):
    """
    >>> selection_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    for i in range(len(nums) - 1):
        minimum = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                minimum = j
        nums[minimum], nums[i] = nums[i], nums[minimum]
    return nums

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
