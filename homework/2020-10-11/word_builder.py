def word_builder(str_lst, int_lst):
    """
    >>> word_builder(["g", "e", "o"], [1, 0, 2])
    'ego'
    >>> word_builder(["e", "t", "s", "t"], [3, 0, 2, 1])
    'test'
    >>> word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])
    'edabit'
    """
    word_lst = [None] * len(int_lst)
    for i in range(len(word_lst)):
        word_lst[i] = str_lst[int_lst[i]]
    return "".join(word_lst)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
