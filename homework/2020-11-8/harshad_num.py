def is_harshad(num):
    """
    >>> is_harshad(481)
    True
    >>> is_harshad(89)
    False
    >>> is_harshad(516)
    True
    >>> is_harshad(200)
    True
    """
    digits = [int(x) for x in str(num)]
    return num % sum(digits) == 0

def is_harshad2(num2):
    """
    >>> is_harshad2(481)
    True
    >>> is_harshad2(89)
    False
    >>> is_harshad2(516)
    True
    >>> is_harshad2(200)
    True
    """
    summed = 0
    nummed = num2
    while nummed != 0:
        remaindered = nummed % 10
        summed += remaindered
        nummed = nummed // 10
    return num2 % summed == 0  

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
