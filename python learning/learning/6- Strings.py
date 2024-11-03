# Metods:

info = " my name is HoSSein raMezani, mmy family is not ok?m"
my_list = ["this" , "is", "a", "random", "text"]

# info = "testing9"

res = info.capitalize() # Every thing except the first letter will be lower case but the first one will be uppercase
res = info.casefold() # makes the characters lower case (for all languages characters)
res = info.lower() # makes the characters lower case (for all Eglish characters only)
res = info.upper() # makes the characters upper case (for all Eglish characters only)
res = info.title() # makes each word start with upper case and conttinue with lower case characters until next word
res = info.swapcase() # tuns upper case to lower case and lower case to upper case

res = info.islower() # returns true if all characters are lower case
res = info.isupper() # returns true if all characters are upper case
res = info.isalpha() # returns true if all characters are alphabet
res = info.isalnum() # returns true if all characters numbers
res = info.istitle() # returns true if all words are started with upper case characters and continues with lower case characters untill nex word
res = info.isascii() # returns true if all characters are from ASCII characters (American Standard Code for Information Interchange)
res = info.isspace() # returns true if all characters are spcae characters (\n, \t, (the spcae itself), etc...)
res = info.isprintable() # returns true if all characters printable (\n, \t and ... are not printable characters, but space " " is!)
res = info.isidentifier() # returns true if the string is a python identifier like if, def, class, ... (the defined keywords) or it could be a vriable name (even not defined yet!)
res = info.isdecimal() # (is usually used) if containing numbers that can be used in programming iguess!! like i cant convert a number with a specific font into an integer with int() function IF it is identified with isdecimal() and otherwise not!
res = info.isdigit() # this catergory of numbers is containing superscript and subscript and other fonts of numbers but they cant be converted to integer values with int() function (is decimal is not included int this type)
res = info.isnumeric() # this category of numbers is containing language base numbers (digit and decimal numbers are not contained)
# isdecimal() ⊆ isdigit() ⊆ isnumeric()
res = info.endswith("ok?", 5, 15) # returns true if the string is ending with the given string. it also accepts two other arguments as start and end of the searching range 
res = info.startswith("ok?", 5, 15) # just like the endwith() but checks if it starts with a string

res = info.center(40, "*") # creates a string with given length and puts the strin in center of the string also filles the spacing in each side with second given string (its length must be 1)
res = info.ljust(40, "*") # just like the center
res = info.rjust(40, "*") # just like the center
res = info.strip() # removes all starting and ending whitespaces (\n, \t, etc. are included)
res = info.rstrip() # removes all whitespaces from right (\n, \t, etc. are included)
res = info.lstrip() # removes all whitespaces from left (\n, \t, etc. are included)
res = info.split("m", maxsplit = 3) # splits the string by spaces or the given string: in case the starting part is seperator and the character is not whitespace or None there will be an empty string in the resaults, and if the seperator is whitespace or None then multiple spaces are concidered as one according to maxsplit
res = info.rsplit("m", maxsplit = 3) # just like the split but from right
res = info.splitlines() # splits the string for each line (\n), if the KeepEnds is true then the \n will not be removed for each list value
res = "*".join(my_list) # inserts the string that the join function is used by in between the given iterable
res = info.replace("my", "your", 1) # replaces the first given string with the second given to the number of third argumlent
res = info.zfill(40) # creates a string with the given length and after putting the string within that length the ramaining characters will be filled with 0 (if length was smaller than the given argument)

res = info.index("my", 0, 20) # finds the starting index of the givven string (if not existed will encounter the ValueError), it will start searching fro/to the given index as the second and third arguments
res = info.rindex("my", 2, len(info)) # just like the index() method but will start from the right (will give the starting point index)
res = info.find("my", 0, 20) # exactly like index but will not raise an error if not found (returns -1 if fail)
res = info.rfind("my", 2, 15) # just like the find() but from right
res = info.count("my") # finds the count of the given string

# res = info.encode() 
# res = info.expandtabs() 
# res = info.maketrans() 
# res = info.rpartition()
# res = info.partition()
# res = info.translate()

print(res)

# testing = res[0]

# test = testing.isprintable()

# print(test)




# test = "a#2"
# res = test.isupper()
# res = test.islower()
# res = test.isalnum()

# res = test.isidentifier()

# print(res)


# specials = "!@#$%^&*_-"
# print(f"ther is no special character in you password: {", ".join(specials)}")

# print(*specials)

# test = "im 1"
# test2 = test

# print(test2)
# test = "im 2"
# print(test2)

# test = "f"

# res = test.isalnum()
# print(res)
# print()

# for i in chr(range(48, 57)):
#     print(i)

# for i in "0987654321":
#     print(ord(i))

# 48-57