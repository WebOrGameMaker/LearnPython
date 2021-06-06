def editor(list_string):
    editing_thing = []
    for i in range(len(list_string)):
        if list_string[i] == '#':
            if len(editing_thing) > 0:
                editing_thing.pop()
        else:
            editing_thing.append(list_string[i])
    return editing_thing

def backspace(s, t):
    """
    >>> backspace("ab#c", "ad#c")
    True
    >>> backspace("a#c", "b")
    False
    >>> backspace("#adf#", "b#fsdf")
    False
    """

    return editor(s) == editor(t)

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
