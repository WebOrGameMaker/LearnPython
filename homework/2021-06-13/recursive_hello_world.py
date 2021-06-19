def Hello_World(n):
    """
    >>> Hello_World(0)

    >>> Hello_World(10)
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    Hello World!
    """
    if n > 0:
        print("Hello World!")
        Hello_World(n - 1)

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
