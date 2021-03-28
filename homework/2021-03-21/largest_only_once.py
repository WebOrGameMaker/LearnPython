import math

def only_once_max(nums):
    """
    >>> only_once_max([])
    -1
    >>> only_once_max([1, 1, 2, 3, 3])
    2
    >>> only_once_max([1, 1, 2, 2, 3, 3])
    -1
    """
    digits = {}
    for i in range(len(nums)):
        if nums[i] not in digits:
            digits[nums[i]] = 1
        else:
            digits[nums[i]] += 1

    largest = -math.inf
    for k, v in digits.items(): # k is the key, v is the value
        if largest < k and v == 1:
            largest = k

    if largest == -math.inf:
        return -1
    return largest

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
        