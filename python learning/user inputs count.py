from os import system

system("cls")
the_values = {}
while True:
    user_input = input("enter a value or cancel: ")
    if user_input == "cancel":
        break

    the_values[user_input] = the_values.setdefault(user_input, 0) + 1

print(the_values)
