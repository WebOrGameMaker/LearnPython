def bubble_sort(nums, reverse=False):
    """
    >>> bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], reverse=True)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    stop = len(nums) - 1 # because it cannot compare the last number to another number
    stop_reversed = -1
    sorted = False
    while not sorted:
        sorted = True
        if reverse == True: 
            for i in range(-1, stop_reversed, -1):
                if nums[i] > nums[i - 1]:
                    sorted = False
                    nums[i], nums[i - 1] = nums [i - 1], nums[i]
        else:
            for i in range(0, stop):
                if nums[i] > nums[i + 1]:
                    sorted = False
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
