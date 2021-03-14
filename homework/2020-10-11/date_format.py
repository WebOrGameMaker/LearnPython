from datetime import datetime   
def format_date(datetime_str):
    """
    >>> format_date('10/10/2020')
    '20201010'
    >>> format_date('12/30/4323')
    '43233012'
    """
    datetime_object = datetime.strptime(datetime_str, "%m/%d/%Y")  # convert a string to datetime
    return datetime_object.strftime("%Y%d%m")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
