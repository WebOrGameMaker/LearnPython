# import statistics
def shortest_continuous_subarray(nums):
    """
    >>> shortest_continuous_subarray([1,2,2,3,1])
    2
    >>> shortest_continuous_subarray([1,2,2,3,1,4,2])
    6
    >>> shortest_continuous_subarray([8,4,3,2,1,8,3,2,1,8,9])
    10
    """
    left, count, right = {}, {}, {}
    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] += 1
        if nums[i] not in left:
            left[nums[i]] = i

    for j in range(len(nums) - 1, -1, -1):
        if nums[j] not in right:
            right[nums[i]] = j 

    max_occurs = 0
    min_length = len(nums)
    for num, occurs in count.items():
        if occurs > max_occurs:
            min_length = right[num] - left[num] + 1
        elif occurs == max_occurs:
            num_length = right[num] - left[num] + 1
            if num_length < min_length:
                min_length = right[num] - left[num] + 1
    return min_length

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
