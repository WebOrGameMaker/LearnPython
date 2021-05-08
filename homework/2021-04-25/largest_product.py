from math import inf
def largest_product(nums):
    """
    >>> largest_product([-10,-6,-5,-3,2,4,5,3,4,5])
    60
    >>> largest_product([-3,-2,1,4,3,1,2,4])
    16
    >>> largest_product([])
    -inf
    """
    largest = -inf
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] * nums[j] > largest:
                largest = nums[i] * nums[j]
    return largest

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
