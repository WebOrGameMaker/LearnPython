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

def find_longest_word2(sentence):
    """
    >>> find_longest_word2("a b c de")
    'de'
    >>> find_longest_word2("a bc def ghij klmno pqrstu vwxyz")
    'pqrstu'
    >>> find_longest_word2("a dog is something")
    'something'
    >>> find_longest_word2("")
    ''
    """
    word_start = 0
    longest_word_start, longest_word_end = 0, 1
    max_length = 0
    for i in range(len(sentence) + 1):
        if i == len(sentence) or sentence[i] == " ":
            word_length = i - word_start
            if word_length > max_length:
                max_length = word_length
                longest_word_start = word_start
                longest_word_end = i
            word_start = i + 1
    return sentence[longest_word_start: longest_word_end]

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
