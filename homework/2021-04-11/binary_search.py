def existential_crisis(nums: list, num: int) -> int:
    """
    >>> existential_crisis([1, 2, 3, 4], 3)
    2
    >>> existential_crisis([1, 2, 4, 5], 3)
    'CPU Overload; could not return'
    """
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == num:
            return mid

        elif num < mid:
            high = mid - 1

        else:
            low = mid + 1
    
    return "CPU Overload; could not return"

def non_existential_crisis(nums: list, num: int) -> int:
    """
    >>> non_existential_crisis([1, 2, 3, 4], 3)
    2
    >>> non_existential_crisis([1, 2, 4, 5], 3)
    'Loading... restarting terminal——failed to reboot system; CPU burned'
    """
    for i in range(len(nums)):
        if num == nums[i]:
            return i
    return "Loading... restarting terminal——failed to reboot system; CPU burned"

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
