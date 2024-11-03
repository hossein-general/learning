from os import system
from package import for_init, three_digit_definder, suffix_definder, is_input_valid

# This program will get inputs from user, containing numbers in integer, and then returning the spelling for that number in persian
# این برنامه از مخاطب یک ورودی عددی گرفته و آن را به صورت حروف می نویسد


# def suffix_


# یک - دو - سه - چهار - پنج - شش - هفت - هشت - نه
# یازده - دوازده - سیزده - چهارده - پانزده - شانزده - هفده - هجده - نوزده
# ده - بیست - سی - چهل - پنجاه - شصت - هفتاد - هشتاد - نود
# صد - دویست - سیصد - چهارصد - پانصد - ششصد - هفتصد - هشتصد - نهصد

# میلیون - بیلیون - تریلیون - کوآدریلیون - کوینتیلیون - سکستیلیون - سپتیلون - اکتیلیون - نانیلیون - دسیلیون - آندسیلیون - دیودسیلیون - تریدسیلیون - کواتیوردسیلیون - کویندسیلیون - سکسدسیلیون - سپتدسیلیون - اُکتودسیلیون - نومدسیلیون -


system("cls")

while False:
    num = input("pls enter your number: ")
    system("cls")

    if num == "cancel":
        break

    # if not is_input_valid():
    #     print("your input is not a valid number, pls enter another one")
    #     continue

    split_count, for_range = for_init(num)

    the_num_parts = []
    temp = []

    for triple_index in range(for_range, 0, -1):
        sliced = num[: split_count - 1]
        temp = [three_digit_definder(sliced), suffix_definder(triple_index)]
        the_num_parts.append("".join(temp))
        split_count = 2
    print(the_num_parts)
    input()

print(three_digit_definder("19"))
print(three_digit_definder("117"))
print(three_digit_definder("999"))
