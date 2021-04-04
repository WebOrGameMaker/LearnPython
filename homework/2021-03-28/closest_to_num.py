import math
def closest_smallest(nums, k):
    closest = -math.inf
    for num in nums:
        if num == k:
            return k
        if num > closest and num <= k:
            closest = num
    return closest

def closest_small_large(nums, k):
    closest_dif = math.inf
    for num in nums:
        if num == k:
            return k
        if abs(num - k) < closest_dif:
            closest_dif = abs(num - k)
            answer = num
    return answer

def closest_to_m(x: int, y: int, m: int) -> int:
    """
    >>> closest_to_m(17, 25, 77)
    76
    >>> closest_to_m(10, 5, 25)
    25
    """
    possible_answers = []
    for x_mult in range(m + 1):
        for y_mult in range(m + 1):
            if y*y_mult + x*x_mult <= m:
                possible_answers.append(y*y_mult + x*x_mult)
    return max(possible_answers)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)