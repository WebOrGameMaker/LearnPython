# I know, this isn't allowed
def hard_add1(num1, num2):
    """
    >>> hard_add1("5125515215521515", "125261616261626")
    '5250776831783141'
    >>> hard_add1("6666666666666666666666666666", "99999999999999999999999")
    '6666766666666666666666666665'
    >>> hard_add1("123456789123456789123456789", "987654321987654321987654329876543")
    '987654445444443445444443453333332'
    """
    return str(int(num1) + int(num2))

def hard_add2(s1, s2):
    """
    >>> hard_add2("5125515215521515", "125261616261626")
    '5250776831783141'
    >>> hard_add2("6666666666666666666666666666", "99999999999999999999999")
    '6666766666666666666666666665'
    >>> hard_add2("123456789123456789123456789", "987654321987654321987654329876543")
    '987654445444443445444443453333332'
    >>> hard_add2("99", "9")
    '108'
    """
    i = -1
    carry = 0
    result = [None] * (max(len(s1), len(s2)) + 1)
    while len(s1) >= -i or len(s2) >= -i:
        if len(s1) >= -i:
            digit1 = int(s1[i])
        else:
            digit1 = 0
        if len(s2) >= -i:
            digit2 = int(s2[i])
        else:
            digit2 = 0
        digit_sum = digit1 + digit2 + carry
        if digit_sum >= 10:
            carry = 1
            result[i] = str(digit_sum - 10)
        else:
            carry = 0
            result[i] = str(digit_sum)
        i -= 1
    if carry == 1:
        result[0] = str(carry)
    else:
        result[0] = '' 
    return "".join(result)

# My dad shortened the one above ^ to make this
def hard_pythonic_version_by_dad(s1, s2):
    """
    >>> hard_pythonic_version_by_dad("5125515215521515", "125261616261626")
    '5250776831783141'
    >>> hard_pythonic_version_by_dad("6666666666666666666666666666", "99999999999999999999999")
    '6666766666666666666666666665'
    >>> hard_pythonic_version_by_dad("123456789123456789123456789", "987654321987654321987654329876543")
    '987654445444443445444443453333332'
    >>> hard_pythonic_version_by_dad("99", "9")
    '108'
    """
    carry, digit1, digit2 = 0, 0, 0
    i = -1
    result = [None] * (max(len(s1), len(s2)) + 1)
    while len(s1) >= -i or len(s2) >= -i:
        digit1 = int(s1[i]) if len(s1) >= -i else 0
        digit2 = int(s2[i]) if len(s2) >= -i else 0
        digit_sum = digit1 + digit2 + carry
        result[i] = str(digit_sum - 10) if digit_sum >= 10 else str(digit_sum)
        carry = 1 if digit_sum >= 10 else 0
        i -= 1
    result[0] = "1" if carry == 1 else ''
    return "".join(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)