def shortest_continuous_subarray(nums):
    """
    >>> shortest_continuous_subarray([1,2,2,3,1])
    2
    >>> shortest_continuous_subarray([1,2,2,3,1,4,2])
    6
    """
    mode = 0
    for num in nums:
        if nums.count(num) > mode:
            mode = num
    for i in range(len(nums)):
        if nums[i] == mode:
            break
        else:
            nums.pop(i)
    for i in range(len(nums)-1, -1, -1): # the stop can't be -1, so it becomes 0
        if nums[i] == mode:
            break
        else:
            nums.pop(i)
    return len(nums)

# Time Complexity: O(n^2)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
