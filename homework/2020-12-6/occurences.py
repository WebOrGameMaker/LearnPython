import doctest
def occurences(*nums):
    """
    >>> occurences(5, 3, 6, 6, 3, 7, 3, 7, 7, 4)
    {5: 1, 3: 3, 6: 2, 7: 3, 4: 1}
    """
    occurence_dict = {}
    for ele in nums:
        if ele in occurence_dict:
            occurence_dict[ele] = occurence_dict[ele] + 1
        else:
            occurence_dict[ele] = 1
    return occurence_dict

if __name__ == "__main__":
    doctest.testmod(verbose=True)
