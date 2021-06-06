def counting_sort(nums):
    """
    >>> counting_sort([4, 2, 2, 8, 3, 3, 1])
    [1, 2, 2, 3, 3, 4, 8]
    """
    size = len(nums)
    output = [0] * size
    count = [0] * (max(nums) + 1)
    # Putting the count into count
    for i in range(size):
        count[nums[i]] += 1

    # Getting the cumulative count
    for j in range(1, len(count)):
        count[j] += count[j-1]

    # Putting the numbers in sorted order into output
    a = size - 1
    while a >= 0:
        output[count[nums[a]] - 1] = nums[a]
        count[nums[a]] -= 1
        a -= 1
    
    # Copying the result into the original list
    for k in range(size):
        nums[k] = output[k]

    return nums

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
