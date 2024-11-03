from package import main_menue


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


# this function will redirect user to the main menue function within the ui package
def main():
    main_menue()


# This function checkes if the program is either ran from this file or is it called from somewhere else, this will prevent function "main" from beeing called from somewhere else
if __name__ == "__main__":
    main()
