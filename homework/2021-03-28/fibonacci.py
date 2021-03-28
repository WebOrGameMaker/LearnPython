def fibonacci_finder(k):
    """
    >>> fibonacci_finder(0)
    0
    >>> fibonacci_finder(1)
    1
    >>> fibonacci_finder(2)
    1
    >>> fibonacci_finder(3)
    2
    >>> fibonacci_finder(4)
    3
    >>> fibonacci_finder(5)
    5
    >>> fibonacci_finder(6)
    8
    >>> fibonacci_finder(7)
    13
    >>> fibonacci_finder(8)
    21
    >>> fibonacci_finder(9)
    34
    >>> fibonacci_finder(10)
    55
    >>> fibonacci_finder(11)
    89
    >>> fibonacci_finder(12)
    144
    >>> fibonacci_finder(13)
    233
    >>> fibonacci_finder(14)
    377
    >>> fibonacci_finder(15)
    610
    >>> fibonacci_finder(16)
    987
    >>> fibonacci_finder(17)
    1597
    >>> fibonacci_finder(18)
    2584
    >>> fibonacci_finder(19)
    4181
    >>> fibonacci_finder(20)
    6765
    >>> fibonacci_finder(21)
    10946
    >>> fibonacci_finder(22)
    17711
    >>> fibonacci_finder(23)
    28657
    >>> fibonacci_finder(24)
    46368
    >>> fibonacci_finder(25)
    75025
    >>> fibonacci_finder(26)
    121393
    >>> fibonacci_finder(27)
    196418
    >>> fibonacci_finder(28)
    317811
    >>> fibonacci_finder(29)
    514229
    >>> fibonacci_finder(30)
    832040
    >>> fibonacci_finder(31)
    1_346_269
    
    # ^ MILLION 😱😱🙀🙀
    """
    if k == 0:
        return 0
    if k == 1:
        return 1
    Tracker, FibonacciNumber, PreviousNumber, PreviousPreviousNumber = 2, 0, 1, 0
    while Tracker < k+1:
        FibonacciNumber = PreviousNumber + PreviousPreviousNumber
        PreviousNumber, PreviousPreviousNumber = FibonacciNumber, PreviousNumber
        Tracker += 1
    return FibonacciNumber

def fibnum(n):
    if n < 0:
        return "Incorrect input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibnum(n-1) + fibnum(n-2)
print(fibnum(9))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
