def bubble_sort(nums):
    """
    >>> bubble_sort([9,8,4,7,3,2])
    [2, 3, 4, 7, 8, 9]
    """
    stop = len(nums) - 1 # because it cannot compare the last number to another number
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, stop):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums
if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
