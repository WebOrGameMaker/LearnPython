# Odd or Even
def odd_or_even(string):
    """
    >>> odd_or_even("apples")
    True
    >>> odd_or_even("pears")
    False
    >>> odd_or_even("cherry")
    True
    """
    if len(string) % 2 == 0:
        return True
    else:
        return False
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
