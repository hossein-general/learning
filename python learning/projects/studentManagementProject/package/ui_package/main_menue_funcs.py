# this was used for creating a documention on parameters of the functions (as right now for function "add_student")
from typing import Callable

from .ui_assistance_funcs import *
from os import system

# region Menue_options
# Main menue options (exit):
# 1- add
# 2- show
# 3- search
# 4- remove
# 5- edit

# add student menue (exit):
# 1- name
# 2- family
# 3- age
# 4- national code
# 5- phone number
# 6- scores

# search options (exit):
# 1- by name
# 2- by family
# 3- by national code
# 4- by phone number

# remove options (exit):
# kind of search but making each search resault an option for removing students

# edit student:
# kind of search but making each search resault an option for removing students
# endregion


# ---------------------------------------------------------------------------------------------
# region GetInfo
# This functions will get all student information from the user and will validate them right away by the help of funcions within the ui_package.
# This functions will only validate input structures and not the duplicate values. the duplicate values or any search base function will be only cheked in Business-Logic layer in backend
# the values gathered will be validated once again in backend for further security


# I think i should get this student values from bl itself each time, as it would have some changes within it
# student values:
# 1- name
# 2- family
# 3- national code
# 4- phone number
# 5- age
# 7- city
# 8- scores
#


# "attrib_name"
# "null_able"
# "is_num"
# "unique"
# "certain_value"
# "range_num_value"
# "length"

# endregion


# ---------------------------------------------------------------------------------
# Varaible Definition

# message texts:
inp_attrib_msg = "pls enter student"  # A variable containng the message sent for getting an input for a attribute

# ---------------------------------------------------------------------------------

def not_matched(message: str) -> None:
    system("cls")
    print(message)


def add_student(attrib_get_func: Callable[[], tuple[dict]]) -> tuple:
    student_attrib = (
        attrib_get_func()
    )  # This will retrieve thelaatest attribute structure from bl

    for attrib_index in range(
        len(student_attrib)
    ):  # This will iterate though the student_attrib
        inp = input(f"d").strip()
        while True:
            if student_attrib[attrib_index]["not_null"]:
                if inp == "":
                    not_matched("this attribute should not be null, pls enter a value")
                    continue


            if student_attrib[attrib_index]["is_decimal"]:
                if not inp.isdecimal():
                    not_matched("your value should only be containing digits")
                    continue


            if num_format := student_attrib[attrib_index]["is_num"]:
                if not (inp := is_num_func(inp, num_format)):
                    not_matched(f"value is not a convertable value to {num_format}")
                    continue
                        

            if value_list := student_attrib[attrib_index]["certain_value"]:
                if inp not in value_list:
                    not_matched(f"value not in list ({", ".join(value_list)})")
                    continue

            if val_rng := student_attrib[attrib_index]["range_num_value"]:
                if not (inp >= val_rng["start_rng"] and inp <= val_rng["end_rng"]):
                    # This not_matched function is getting a string in using .format instead of fstring just to review the use of the that method
                    not_matched("your value is out of range ({start}, {end})".format(start= val_rng["start_rng"], end = val_rng["end_rng"]))
                    continue

            if val_length := student_attrib[attrib_index]["length"]:
                if not(len(inp) >= val_length["min_len"] and len(inp) <= val_length["max_len"]):
                    # This not_matched argument is checking if the it should say "between a and b" or "a". I think it would have been better if i used a simple if-else statement
                    not_matched(
                        f"your input length must be {f"between {" and ".join(list(val_length.values()))}" if val_length["min_len"] == val_length["max_len"] else val_length["min_len"]} chars"
                        )
                    continue

            # Im not sure if thats a good idea to check users list two times once in ui and once in bl, but ill put it anyway
            if student_attrib[attrib_index]["unique"]:
                # here i
                student_attrib[attrib_index]["name"]

            break 


def show_student():
    pass


def serach_student():
    pass


def remove_student():
    pass


def edit_student():
    pass

    # for index, attrib in enumerate(student_attrib): # This will iterate though the student_attrib
    #     inp = input(f"{inp_attrib_msg} {attrib}: ")

    # {inp_attrib_msg} {student_attrib[attrib_index]["name"]}:


# while True:
#     test = input("num: ")
#     print()

#     if (test.count(".") == 1 or test.count(".") == 0) and (
#         not test.startswith(".") and not test.endswith(".")
#     ):
#         for part in test.split("."):
#             if not part.isdecimal():
#                 break
#         else:
#             test = float(test)
#         pass
#         # continue
#     else:
#         pass
#         # continue
#     print(type(test))

# if test.isdecimal():
#     print("isdecimal")

# if test.isdigit():
#     print("isdigit")

# if test.isnumeric():
#     print("isnumeric")

# print("none")


# while True:
#     val = input("num: ")

#     if (val.count(".") == 1 or val.count(".") == 0) and (
#         not val.startswith(".") and not val.endswith(".")
#     ):
#         for part in val.split("."):
#             if not part.isdecimal():
#                 break

#         else:
#             print("true")
#             continue

#         print("False")
#         continue

#     else:
#         print("False")
#         continue

# test = 2

# match test:
#     case 1:
#         print(test)
#         input()
#     case 2:
#         print(test)
#         input()
#         test = 1
#         continue
#     case 3:
#         print(test)
#         input()
#     case 4:
#         print(test)
#         input()
#     case _:
#         print("none")


# this part was used for is_num part before creating a seperated function for it
            # match num_format:
            #     case "int":
            #         if inp.isdecimal():
            #             inp = int(inp) 
            #         else: 
            #             continue
            #     case "float":
            #         if isfloat(inp):
            #             inp = float(inp) 
            #         else: 
            #             continue
test=2