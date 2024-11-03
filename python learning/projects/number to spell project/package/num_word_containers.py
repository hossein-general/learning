




# suffix, number_spelling, ten_base_nums
spellings = {
    "persian": {
        "s": ("", "هزار", "میلیون", "میلیارد", "بیلیون", "بیلیارد", "تریلیون", "تریلیارد", "کوآدریلیون", "کادریلیارد", "کوینتیلیون",
            "کوانتینیارد", "سکستیلیون", "سکستیلیارد", "سپتیلیون", "سپتیلیارد", "اکتیلیون", "اکتیلیارد", "نانیلیون", "نانیلیارد", ),

        "n": (
            ("", "صد", "دویست", "سیسصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"),
            ("", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"),
            ("", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"),
        ), 

        "t": ("ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده", )}
}

def word_return(language: str, snt : str = "snt") -> tuple:
    """this function will return the word list of numbers, so other functions could use that for their number generation

    Args:
        language (str): this argument contains the language name that we want to use
        snt (str, optional): its a string that contains one of the three letter s: suffix, n: number words and t: ten base numbers. Defaults to "snt".

    Raises:
        ValueError: if the language input was not a string withing the owned keys
        ValueError: if snt value was other than s, n, t or snt itself

    Returns:
        tuple: a tuple containing the requested language number words
    """

    if language not in spellings:
        raise ValueError("your value was out of defined range (should be a language)")
        
    if snt in ("s", "n", "t"):
        return(spellings[language][snt])
    
    elif snt == "snt":
        return(spellings[language])
    
    else:
        raise ValueError("your value was out of defined range (s, n, t)")
    
