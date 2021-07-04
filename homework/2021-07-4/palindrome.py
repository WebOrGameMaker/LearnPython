def palindrome(word: str):
    """
    >>> palindrome("tacocat")
    True
    >>> palindrome("ratattatar")
    True
    >>> palindrome("324432")
    False
    >>> palindrome("3")
    True
    """
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1]) # [start(inclusive):stop(exclusive):step]
        return False

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
