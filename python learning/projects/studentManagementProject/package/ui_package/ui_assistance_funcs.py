

def isfloat(val: str) -> bool:
    if (val.count(".") == 1 or val.count(".") == 0) and (
        not val.startswith(".") and not val.endswith(".")
    ):
        for part in val.split("."):
            if not part.isdecimal():
                return False

        else:
            return True

    else:
        return False



def is_num_func(val: str, number_formatting: str) -> None | int | float:
    match number_formatting:
        case "int":
            if val.isdecimal():
                return int(val) 
        case "float":
            if isfloat(val):
                return float(val) 
    
    return None # This one wasnt necessary as the default return of functions are None, but i think it help to clarify that there was no correct value passed to this function

# def user_input_check():
#     pass