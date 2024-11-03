from .num_word_containers import word_return


def three_digit_definder(slice_: str) -> str:
    """this function will get a string containing up to 3 digits of numbers and will return a spelled version of that

    Args:
        slice_ (str): the slice of the number that will be spelled

    Raises:
        TypeError: if any type other than string is given
        ValueError: if the value wasnt all nums

    Returns:
        str: the spelled version of the number
    """
    if not isinstance(slice_, str):
        raise TypeError("your value must be a string")

    slice_ = slice_.strip()

    if not slice_.isdecimal():
        raise ValueError("the value must be a decimal string")

    slice_ = slice_.zfill(3)

    # TODO
    ten_base_nums = word_return("persian", "t")
    number_spelling = word_return("persian", "n")

    spelled = []
    is_ten_base = False
    for index_, digit_ in enumerate(slice_):
        if digit_ == "0":
            continue

        if index_ == 1 and digit_ == "1":
            is_ten_base = True
            continue

        if spelled:
            spelled.append(" و ")

        if is_ten_base:
            spelled.append(ten_base_nums[int(digit_)])
            continue

        spelled.append(number_spelling[index_][int(digit_)])

    return "".join(spelled)


def suffix_definder(the_triple_index: int) -> str:
    if not isinstance(the_triple_index, int):
        raise TypeError("only integer types are allowed")

    suffix = word_return("persian", "s")

    return suffix[the_triple_index - 1]
