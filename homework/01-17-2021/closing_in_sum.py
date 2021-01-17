def closing_in_sum(num):
    """
    >>> closing_in_sum(2520)
    72
    >>> closing_in_sum(121)
    13
    >>> closing_in_sum(1039)
    22
    >>> closing_in_sum(22225555)
    100
    """
    answer = 0
    first_num = 0
    last_num = -1
    num_lst = list(str(num)) # turns it into a list of strings of numbers
    while len(num_lst) > 0:  
        answer += int(num_lst[first_num])*10 + int(num_lst[last_num]) # takes the first number and multiplies it by 10, takes the second number and adds it to the first number
        del num_lst[first_num]
        del num_lst[last_num]
        if len(num_lst) == 1: # checks if there is only one number left
            answer += int(num_lst[first_num])
            del num_lst[first_num]
    return answer

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)