from copy import copy, deepcopy
from os import system

system("cls")
old_list = ["Hellow", True, 3, 4.1, ["one", "two", "three"]]

# ------------{NOT COPY}------------
# new_list = old_list
# new_list = ["Hellow", True, 3, 4.1, ["one", "two", "three"]]


# ------------{SHALLOW COPY}------------
# new_list = copy(old_list)
# new_list = old_list.copy()

# ------------{DEEP COPY}------------
new_list = deepcopy(old_list)


print(id(old_list), ": ", old_list)
print(id(new_list), ": ", new_list)
print("are they the same? ", old_list is new_list)
print("do they have the same value? ", old_list == new_list)
print()

print("-------------------------")

old_list[0] = "Goodby"
old_list[4].append("four")
old_list.append("Wow!!")


print(id(old_list), ": ", old_list)
print(id(new_list), ": ", new_list)
# print("are they the same? ", old_list is new_list)
# print("do they have the same value? ", old_list == new_list)
print()
