

def for_init(string_num: str) -> tuple:
    """This functioin will get a string as an input which is the number that will be splitted and returns the number of 3x numbers within that number

    Args:
        string_num (str): the number that will be splited

    Raises:
        TypeError: if the input variable type was not string

    Returns:
        tuple: returns a tuple of 3x numbers (four_count) and first slice count (slice_count) to then be unpacked and used
    """
    if not isinstance(string_num, str):
        raise TypeError(
            "this function will accept a string of digits as an argument")

    for_count = (len(string_num) // 3) + 1
    slice_count = len(string_num) % 3
    return (slice_count, for_count)



