def next_letter_word(string):
    """
    >>> next_letter_word("hello")
    'ifmmp'
    >>> next_letter_word("bye")
    'czf'
    >>> next_letter_word("welcome")
    'xfmdpnf'
"""
    lst = [None] * len(string)
    for i in range(len(string)):
        if string[i] == 'z':
            string[i] = 'a'
        elif string[i] == 'Z':
            string[i] = 'A'
        else:
            lst[i] = chr(ord(string[i]) + 1)
    return ''.join(lst)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
