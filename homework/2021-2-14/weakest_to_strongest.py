def weakest_to_strongest(rows, weakest_rows):
    """
    >>> weakest_to_strongest([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3)
    [2, 0, 3]
    >>> weakest_to_strongest([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2)
    [0, 2]
    """
    tracker = 0
    weakest_indexes = []
    soldiers_in_each_row = []
    for i in range(len(rows)):
        soldiers_in_each_row.append(tuple((sum(rows[i]), i)))
    soldiers_in_each_row.sort()    
    while tracker < weakest_rows:
        weakest_indexes.append((soldiers_in_each_row[tracker])[1])
        tracker += 1
    return weakest_indexes

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
