def shortest_continuous_subarray(nums):
    """
    >>> shortest_continuous_subarray([1,2,2,3,1])
    2
    >>> shortest_continuous_subarray([1,2,2,3,1,4,2])
    6
    >>> shortest_continuous_subarray([8,4,3,2,1,8,3,2,1,8,9])
    10
    """
    mode = 0
    for num in nums:
        if nums.count(num) > mode:
            mode = num
    for i in range(len(nums)):
        if nums[i] == mode:
            break
    for j in range(len(nums)-1, -1, -1): # the stop can't be -1, so it becomes 0
        if nums[j] == mode:
            break
    return j - i + 1

# Time Complexity: O(n^2)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
