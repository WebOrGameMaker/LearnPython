# def subsequent_loop(small_word, large_word):
#     s, l = 0, 0
#     while s < len(small_word) and l < len(large_word):
#         if small_word[s] == large_word[l]:
#             s += 1
#         l += 1
    
#     return s == len(small_word)
 
# print(subsequent_loop("hca", "cathartic"))
# print(subsequent_loop("hac", "cathartic"))

def _subsequent_recursion(small_word, large_word, s, l):
    if s == len(small_word):
        return True
    if l == len(large_word):
        return False
    if small_word[s] == large_word[l]:
        return _subsequent_recursion(small_word, large_word, s + 1, l + 1)
    return _subsequent_recursion(small_word, large_word, s, l + 1)

def is_subsequent_recursion(small_word, large_word):
    """
    >>> is_subsequent_recursion("hac", "cathartic")
    True
    >>> is_subsequent_recursion("cat", "tack")
    False
    """
    return _subsequent_recursion(small_word, large_word, 0, 0)

if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)

sum()
