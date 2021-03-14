def letters_only(string):
    """
    >>> letters_only("PYTHON")
    False
    >>> letters_only("python")
    True
    >>> letters_only("12321313")
    False
    >>> letters_only("i have spaces")
    True
    >>> letters_only("i have numbers(1-10)")
    False
    >>> letters_only("")
    False
    """
    if len(string) == 0:
        return False
    else:
        for char in string:
            if (char < 'a' or char > 'z') and char != ' ':  # not(char.isalpha() and char.islower() or char.isspace()) is another wae
                return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
