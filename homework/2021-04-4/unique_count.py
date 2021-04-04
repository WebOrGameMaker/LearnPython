def unique_count(nums):
    """
    >>> unique_count([1, 2, 2, 3, 3, 3])
    True
    >>> unique_count([1, 2, 2, 3, 3, 3, 4])
    False
    """
    count = {} # collections.Counter(nums)
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    unique = True
    if len(set(count.values())) < len(count.values()):
        unique = False
    return unique
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
