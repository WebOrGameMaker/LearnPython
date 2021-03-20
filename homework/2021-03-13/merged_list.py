def merged_list(nums1, nums2):
    """
    >>> merged_list([1, 2, 3], [2, 5, 6])
    [1, 2, 2, 3, 5, 6]
    >>> merged_list([1, 3, 5, 7, 9], [2, 4, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> merged_list([3, 3, 5, 5, 8, 8, 9], [2, 3, 3, 4, 4, 7, 7, 7, 8, 9, 9, 9])
    [2, 3, 3, 3, 3, 4, 4, 5, 5, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
    """
    i = 0
    j = 0
    sorted_combined_nums = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            sorted_combined_nums.append(nums1[i])
            i += 1
        else:
            sorted_combined_nums.append(nums2[j])
            j += 1

    while i < len(nums1):
        sorted_combined_nums.append(nums1[i])
        i += 1

    while j < len(nums2):
        sorted_combined_nums.append(nums2[j])
        j += 1

    return sorted_combined_nums        

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(sorted()) # this is for if you want to write a long test case by spamming and want to sort it