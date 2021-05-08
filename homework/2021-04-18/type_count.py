# Things to remember:
# Upper Bound: list[middle] > target
# Lower Bound: list[middle] >= target

def negative_count(nums):
    """
    >>> negative_count([-4,-3,-1,1,2,2,3])
    3
    >>> negative_count([1,2,2,3,4])
    0
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= 0: # Lower Bound
            high = mid
        else:
            low = mid + 1
    return low

def non_positive_count(nums):
    """
    >>> non_positive_count([-3,-3,-2,-1,0,1,2,3])
    5
    >>> non_positive_count([-3,-2,-1,1,1,2])
    3
    >>> non_positive_count([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])
    0
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > 0: # Upper Bound
            high = mid
        else:
            low = mid + 1
    return low

def positive_count(nums):
    """
    >>> positive_count([-5,-3,-2,-1,0,1,2,3,3])
    4
    >>> positive_count([-3,-2,-1])
    0
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > 0:
            high = mid
        else:
            low = mid + 1
    return len(nums) - low

def non_negative_count(nums):
    """
    >>> non_negative_count([-3,-3,-2,-1,0,1,2,3,3,4])
    6
    >>> non_negative_count([-2,-1,-1])
    0
    """
    high = len(nums)
    low = 0
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] >= 0:
            high = mid
        else:
            low = mid + 1
    return len(nums) - low
            
if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
        