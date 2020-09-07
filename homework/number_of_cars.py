def cars_for(people):
    """
    >>> cars_for(5)
    1
    >>> cars_for(11)
    3
    >>> cars_for(0)
    0
    """

    cars = 0
    for _ in range(people, 0, -5):
        cars += 1
    return cars

def cars_for_reversed(people):
    """
    >>> cars_for_reversed(5)
    1
    >>> cars_for_reversed(11)
    3
    >>> cars_for_reversed(0)
    0
    """

    cars = 0
    for _ in range(0, people, 5):
        cars += 1
    return cars

def cars_while(people):
    """
    >>> cars_while(5)
    1
    >>> cars_while(11)
    3
    >>> cars_while(0)
    0
    """

    cars = 0
    i = people
    while i > 0:
        cars += 1  # need one more car if there are any people
        i += -5  # one car can have 5 people. This is how many people remain.
    return cars

def cars_math(people):
    """
    >>> cars_while(5)
    1
    >>> cars_while(11)
    3
    >>> cars_while(0)
    0
    """

    cars = people // 5  # find the quotient
    remainder = people % 5  # module operator.
    if people > 0 and remainder > 0:
        cars += 1
    return cars

def cars_divmod(people):
    """
    >>> cars_while(5)
    1
    >>> cars_while(11)
    3
    >>> cars_while(0)
    0
    """

    cars, remainder = divmod(people, 5)  # find the quotient and remainder in a single function call
    if people > 0 and remainder > 0:
        cars += 1
    return cars

if __name__ == "__main__":
    import doctest
    doctest.testmod()
