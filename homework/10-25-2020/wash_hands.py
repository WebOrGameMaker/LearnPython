def wash_hands(times_washed, num_months_followed):
    """
    >>> wash_hands(8, 7)
    '588 minutes and 0 seconds'
    >>> wash_hands(0, 0)
    '0 minutes and 0 seconds'
    >>> wash_hands(7, 9)
    '661 minutes and 30 seconds'
    """
    total_washed_seconds = (times_washed * num_months_followed) * 21 * 30
    minutes = total_washed_seconds // 60
    seconds = total_washed_seconds - minutes * 60
    return f"{minutes} minutes and {seconds} seconds"

def wash_hands_divmod(times_washed, num_months_followed):
    """
    >>> wash_hands(8, 7)
    '588 minutes and 0 seconds'
    >>> wash_hands(0, 0)
    '0 minutes and 0 seconds'
    >>> wash_hands(7, 9)
    '661 minutes and 30 seconds'
    """
    minutes, seconds = divmod((times_washed * num_months_followed) * 21 * 30, 60)
    return f"{minutes} minutes and {seconds} seconds"

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)