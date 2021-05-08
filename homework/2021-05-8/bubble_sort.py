def bubble_sort_move_largest(nums):
    """
    >>> bubble_sort_move_largest([10, 3, 9, 2, 5, 7, 2, 1])
    [1, 2, 2, 3, 5, 7, 9, 10]
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

def bubble_sort_move_smallest(nums):
    """
    >>> bubble_sort_move_smallest([10, 9, 1, 8, 6, 4, 3, 5, 7, 2])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    stop = -len(nums)
    sorted = False
    while not sorted:
        sorted = True
        for i in range(-1, stop, -1):
            if nums[i] < nums[i - 1]:
                sorted = False
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)