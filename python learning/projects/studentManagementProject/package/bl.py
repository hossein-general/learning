# 1- name
# 2- family
# 3- national code
# 4- phone number
# 5- age
# 6- gender
# 7- city
# 8- scores


# student attributes: (0 attribute variable name, 1 attribute input text, 2 null-able, 3 is-num, 4 has validation range, 5 str-rng, 6 end-rng, 7 has available list, 8 available range, 9 has exact length, 10 exact length, 11 is-uniq, )

# 0 first name, 1 last name, 2 age, 3 national code, 4 phone number, 5 gender, 6 c_sharp, 7 java, 8 python


# ---------------------------------------------------------------------------------
# Varaible Definition

# This variable will be containing all needed information about each student attribute

# student_attributes = {
#     "name": {
#         "not_null": False,
#         "is_num": False,
#         "unique": False,
#         "certain_value": None,
#         "range_num_value": None,
#         "length": (3, 15),
#     },
#     "last name": {
#         "not_null": False,
#         "is_num": False,
#         "unique": False,
#         "certain_value": None,
#         "range_num_value": None,
#         "length": (3, 15),
#     },
#     "national code": {
#         "not_null": False,
#         "is_num": False,
#         "unique": True,
#         "certain_value": None,
#         "range_num_value": None,
#         "length": (10, 10),
#     },
#     "phone number": {
#         "not_null": True,
#         "is_num": False,
#         "unique": True,
#         "certain_value": None,
#         "range_num_value": None,
#         "length": (11, 11),
#     },
#     "age": {
#         "not_null": False,
#         "is_num": True,
#         "unique": False,
#         "certain_value": None,
#         "range_num_value": (18, 150),
#         "length": None,
#     },
#     "gender": {
#         "not_null": False,
#         "is_num": False,
#         "unique": False,
#         "certain_value": ("male", "female"),
#         "range_num_value": None,
#         "length": None,
#     },
#     "city": {
#         "not_null": False,
#         "is_num": False,
#         "unique": False,
#         "certain_value": ("tehran", "mashhad", "esfehan", "karaj"),
#         "range_num_value": None,
#         "length": None,
#     },
# }

student_attributes = (
    {
        "attrib_name": "name",
        "not_null": False,
        "is_decimal": False,
        "is_num": False,
        "unique": True,
        "certain_value": None,
        "range_num_value": None, # if the value is between two numbers (e.g. 23 is between age 18 and 150)
        "length": {"min": 3, "max": 15}, # if the value has a length (e.g. 3 up to 15 character)
    },
    {
        "attrib_name": "last name",
        "not_null": False,
        "is_decimal": False,
        "is_num": False,
        "unique": False,
        "certain_value": None,
        "range_num_value": None,
        "length": {"min": 3, "max": 15},
    },
    {
        "attrib_name": "national code",
        "not_null": False,
        "is_decimal": True,
        "is_num": False,
        "unique": True,
        "certain_value": None,
        "range_num_value": None,
        "length": {"min": 10, "max": 10},
    },
    {
        "attrib_name": "phone number",
        "not_null": True,
        "is_decimal": True,
        "is_num": False,
        "unique": True,
        "certain_value": None,
        "range_num_value": None,
        "length": {"min": 11, "max": 11},
    },
    {
        "attrib_name": "age",
        "not_null": False,
        "is_decimal": True,
        "is_num": "int",
        "unique": False,
        "certain_value": None,
        "range_num_value": {"start_rng": 18, "end_rng": 150},
        "length": None,
    },
    {
        "attrib_name": "gender",
        "not_null": False,
        "is_decimal": False,
        "is_num": False,
        "unique": False,
        "certain_value": ("male", "female"),
        "range_num_value": None,
        "length": None,
    },
    {
        "attrib_name": "city",
        "not_null": False,
        "is_decimal": False,
        "is_num": False,
        "unique": False,
        "certain_value": ("tehran", "mashhad", "esfehan", "karaj"),
        "range_num_value": None,
        "length": None,
    },
)

# ---------------------------------------------------------------------------------

def get_attrib_list0() -> tuple[dict]:
    """returnes the latest student attribute list for validations

    Returns:
        tuple[dict]: a student attribute list containing dictionaries of attributes information
    """
    return student_attributes


# TODO
# This function will check if the argument sent is duplicate within the given attribute scope (for example phone number or national code)
def check_duplicate(val: str | int | float, attrib_name: str) -> bool:
    pass





