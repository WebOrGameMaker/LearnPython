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
    else: # optional
        return False
        
# Odd or Even reversed
def odd_or_even_reverse(string):
    """
    >>> odd_or_even_reverse("apples")
    True
    >>> odd_or_even_reverse("pears")
    False
    >>> odd_or_even_reverse("cherry")
    True
    """
    if len(string) % 2 == 1:
        return False
    else: # optional
        return True
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
