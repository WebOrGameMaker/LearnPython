def decimal_int(str_binary):
    """
    >>> decimal_int("110101010101010101001010001")
    111848017
    >>> decimal_int("110101010010101010110")
    1746262
    >>> decimal_int("111110000111001")
    31801
    """
    answer = 0
    multiplier = 1
    for i in range(len(str_binary) - 1, -1, -1):
        answer += int(str_binary[i]) * multiplier
        multiplier  *= 2
    return answer

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
