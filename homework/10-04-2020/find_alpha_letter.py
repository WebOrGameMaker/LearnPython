def is_letter(char):
    """
    >>> is_letter('C')
    True
    >>> is_letter('a')
    True
    >>> is_letter('4')
    False
    """
    return char.isalpha()

def has_letter(string):
    """
    >>> has_letter('3k2h4kj2l3h4l23k4')
    True
    >>> has_letter('093798247290384723847234a')
    True
    >>> has_letter('213024834324')
    False
    """
    for char in string:
        if is_letter(char):
            return True
    return False

def find_alpha_strings(lst):
    """
    >>> find_alpha_strings(['John', ' ', 'Amanda', 5])
    ['John', 'Amanda']
    """
    output = []
    for ele in lst:
        if isinstance(ele, str) and has_letter(ele):  # type(ele) == str is another wae to tell if ele is string
            output.append(ele)
    return output

def combined_version(lst):
    """
    >>> combined_version(['John', ' ', 'Amanda', 5])
    ['John', 'Amanda']
    """
    output = []
    for ele in lst:
        if isinstance(ele, str):  # type(ele) == str is another wae to tell if ele is string
            for char in ele:
                if char.isalpha():
                    output.append(ele)
                    break
    return output

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
