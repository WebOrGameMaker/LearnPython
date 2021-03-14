def neutralize1(str1, str2):
    """
    >>> neutralize1("--++--", "++--++")
    '000000'
    >>> neutralize1("-+-+-+", "-+-+-+")
    '-+-+-+'
    >>> neutralize1("-++-", "-+-+")
    '-+00'
    """
    to_be_joined_output = []
    for i in range(len(str1)): # str1 AND str2's length are the same, so both are usable 
        to_be_joined_output.append(str1[i] if str1[i] == str2[i] else "0")

def neutralize2(str1, str2):
    """
    >>> neutraliz2("--++--", "++--++")
    '000000'
    >>> neutralize2("-+-+-+", "-+-+-+")
    '-+-+-+'
    >>> neutralize2("-++-", "-+-+")
    '-+00'
    """
    to_be_joined_output = []
    for i in range(len(str1)): # str1 AND str2's length are the same, so both are usable 
        if str1[i] == str2[i]:
            new_char = str1[i]
        else:
            new_char = "0"
        to_be_joined_output.append(new_char)

def neutralize3(str1, str2):
    """
    >>> neutralize3("--++--", "++--++")
    '000000'
    >>> neutralize3("-+-+-+", "-+-+-+")
    '-+-+-+'
    >>> neutralize3("-++-", "-+-+")
    '-+00'
    """
    to_be_joined_output = []
    for i in range(len(str1)): # str1 AND str2's length are the same, so both are usable 
        if str1[i] == '+' and str2[i] == '+':
            to_be_joined_output.append('+')
        if str1[i] == '-' and str2[i] == '+':
            to_be_joined_output.append('0')
        if str1[i] == '+' and str2[i] == '-':
            to_be_joined_output.append('0')
        if str1[i] == '-' and str2[i] == '-':
            to_be_joined_output.append('-')
    return ''.join(to_be_joined_output)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)