# Number of Cars needed
# 1
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

# 2
def cars_for_range_reversed(people):
    """
    >>> cars_for_range_reversed(5)
    1
    >>> cars_for_range_reversed(11)
    3
    >>> cars_for_range_reversed(0)
    0
    """

    cars = 0
    for _ in range(0, people, 5):
        cars += 1
    return cars

# 3
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

# 4
def cars_math(people):
    """
    >>> cars_while(5)
    1
    >>> cars_while(11)
    3
    >>> cars_while(0)
    0
    """

    cars = people // 5  # find the quotient with remainder
    remainder = people % 5  # module operator
    if people > 0 and remainder > 0:
        cars += 1
    return cars

# 5
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

# importing doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# End of code