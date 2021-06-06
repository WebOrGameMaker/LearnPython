def duplicate_remover(word):
    """
    >>> duplicate_remover("abbaca")
    'ca'
    >>> duplicate_remover("azxxzy")
    'ay'
    """
    stack = []
    for t in word:
        if len(stack) == 0:
            stack.append(t)
        elif t == stack[-1]:
            stack.pop()
        else:
            stack.append(t)
    return "".join(stack)

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
