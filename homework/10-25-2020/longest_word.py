def find_longest_word(string):
    """
    >>> find_longest_word("Margaret's toy is a pretty doll.")
    "Margaret's"
    >>> find_longest_word("A thing of beauty is a joy forever.")
    'forever.'
    >>> find_longest_word("Forgetfulness is by all means powerless!")
    'Forgetfulness'
    """
    lst = string.split()
    if len(lst) == 0:
        return None
    largest_word = lst[0]
    for word in lst:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
