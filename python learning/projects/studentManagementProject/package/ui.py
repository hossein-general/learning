from os import system
from ui_package import (
    user_input_check,
    add_student,
    show_student,
    serach_student,
    remove_student,
    edit_student,
)
from .bl import get_attrib_list


# region TEST

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

# ---------------------------------------------------------------------------------
# Varaible Definition

str_main_menue = """pls enter your choice as a number:
1- add
2- show
3- search
4- remove
5- edit

(1-5 / Exit): """

str_add_student_menue = """pls enter student: """

# This variable is no longer needed as its combined with menue_funcs variables
# menue_choices = {"1", "2", "3", "4", "5"}  # values for main menue options

# Main menue functions from ui package stored in a tuple, also the needed arguments for them to pass(as right now its only the need of attribute list), also the number they have in the menue list
menue_funcs = {
    "1": {"func": add_student, "needs_list": True},
    "2": {"func": show_student, "needs_list": False},
    "3": {"func": serach_student, "needs_list": False},
    "4": {"func": remove_student, "needs_list": False},
    "5": {"func": edit_student, "needs_list": False},
}
# ---------------------------------------------------------------------------------


# This main menue function only directs user to the relavant function within the main_menue_functions and all inputs needed for those functions are handled there
def main_menue():
    system(
        "cls"
    )  # This clear screen is only used once befor the progrmas main menue is not started

    while True:  # A while loop that doesnt end unless user wants
        mm_input = input()  # Gettint the main menue option value from user
        if mm_input in (menue_funcs):
            menue_funcs[mm_input](get_attrib_list if menue_funcs[mm_input]["needs_list"] == True else None)

        
        
        # Old version of function caller:
        # if mm_input in (menue_choices):  # Checking if the value is not out of range
        #     menue_funcs[int(mm_input) - 1](get_attrib_list)  # Calling the relevant function

        if mm_input == "cancel":
            break
