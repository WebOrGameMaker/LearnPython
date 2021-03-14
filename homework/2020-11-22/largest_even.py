def largest_even(num_lst):
    """
    >>> largest_even([3, 7, 2, 1, 7, 9, 10, 13])
    10
    >>> largest_even([1, 3, 5, 7])
    -1
    >>> largest_even([0, 19, 18973623])
    0
    >>> largest_even([1, 4, 2])
    4
    """
    largest_even_num = -1
    for i in range(len(num_lst)):
        if num_lst[i] % 2 == 0 and num_lst[i] > largest_even_num:
            largest_even_num = num_lst[i]
    return largest_even_num

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)