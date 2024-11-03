from os import system

system("cls")


# student attributes: (0 attribute variable name, 1 attribute input text, 2 null-able, 3 is-num, 4 has validation range,
# 5 str-rng, 6 end-rng, 7 has available list, 8 available range, 9 has exact length, 10 exact length, 11 is-uniq, )

# 0 first name, 1 last name, 2 age, 3 national code, 4 phone number, 5 gender, 6 c_sharp, 7 java, 8 python
student_attributes = (
    (
        "first_name",
        "first name: ",
        False,
        False,
        False,
        None,
        None,
        False,
        (),
        False,
        None,
        False,
    ),  # 1
    (
        "last_name",
        "last name: ",
        False,
        False,
        False,
        None,
        None,
        False,
        (),
        False,
        None,
        False,
    ),  # 2
    ("age", "age: ", True, True, True, 18, 150, False, (), False, None, False),  # 3
    (
        "nationalcode",
        "nationalcode: ",
        False,
        False,
        False,
        None,
        None,
        False,
        (),
        True,
        2,
        True,
    ),  # 4
    (
        "phone_number",
        "phone number: ",
        True,
        False,
        False,
        None,
        None,
        False,
        (),
        True,
        4,
        False,
    ),  # 5
    (
        "gender",
        "gender: ",
        True,
        False,
        False,
        None,
        None,
        True,
        ("male", "female"),
        False,
        None,
        False,
    ),  # 6
    ("c_sharp", "C#: ", True, True, True, 0, 100, False, (), False, None, False),  # 7
    ("java", "java: ", True, True, True, 0, 100, False, (), False, None, False),  # 8
    (
        "python",
        "python: ",
        True,
        True,
        True,
        0,
        100,
        False,
        (),
        False,
        None,
        False,
    ),  # 9
)

menue = (
    "1- Add student \n2- Show student \n3- Remove\n4- Search\n5- Best Score\n\n(1-5): "
)
students_list = [
    ("Hossein", "Ramezani", 20, "10", "0990", "male", 50, 23, 90),
    ("Mohammad", "Rajabi", 20, "11", "0912", "male", 20, 90, 30),
    ("Mahsa", "seyfi", 22, "12", "0936", "female", 90, 50, 20),
    ("Ali", "Rahimi", 30, "13", "0919", "male", 90, 50, 90),
]

while True:
    choice = input(menue)
    system("cls")

    match choice:
        case "1":  # Add Student
            student_maker = [None] * 9
            for index, attribute in enumerate(student_attributes):
                while True:
                    temp_val = input(attribute[1])

                    if temp_val:
                        # TODO: make a validation for intger input values
                        if attribute[3]:
                            temp_val = int(temp_val)

                        if attribute[4] and (
                            temp_val not in range(attribute[5], attribute[6] + 1)
                        ):
                            system("cls")
                            print(
                                f"pls enter a number within the rang ({attribute[5]}-{attribute[6]})"
                            )
                            continue

                        if attribute[11]:
                            is_duplicate = False
                            for student in students_list:
                                if temp_val == student[index]:
                                    system("cls")
                                    print(
                                        f'the national code "{temp_val}" is already assigned to {student[0]} {student[1]}'
                                    )
                                    is_duplicate = True
                                    break
                            if is_duplicate:
                                continue

                        if attribute[7] and (temp_val not in attribute[8]):
                            system("cls")
                            print("pls enter a valid gender (male/female)")
                            continue

                        if attribute[9] and (len(temp_val) != attribute[10]):
                            system("cls")
                            print(
                                f"this attribute should be {attribute[10]} characters"
                            )
                            continue

                    elif not attribute[2]:
                        system("cls")
                        print("pls dont leave this field empty")
                        continue

                    break

                system("cls")
                student_maker[index] = temp_val
            print("Notif: student added sucessfully: ", student_maker)
            students_list.append(tuple(student_maker))

        case "2":  # Show Students
            answers_list = []
            for index, attribute in enumerate(student_attributes):
                cancel = False
                all_attributes = False
                while True:
                    answer = input(
                        f"Do you want to show {attribute[0]}? (yes/no/cancel/all): "
                    )
                    system("cls")
                    match answer:
                        case "yes" | "YES" | "y" | "Y":
                            answers_list.append(index)
                            break

                        case "no" | "NO" | "n" | "N":
                            break

                        case "cancel" | "CANCEL":
                            cancel = True
                            break

                        case "all" | "ALL":
                            answers_list = [
                                i for i in range(0, len(student_attributes))
                            ]
                            all_attributes = True
                            break

                        case _:
                            print("sorry i dont get it, what did you say again?")
                if cancel or all_attributes:
                    break

            if not cancel:
                for student in students_list:
                    for index in answers_list:
                        print(student[index], end=" - ")
                    print()
                input("\npress enter to continue... ")
                system("cls")

        case "3":  # Remove Student
            while True:
                student_nc = input("pls enter the student national code to delete: ")
                if len(student_nc) != student_attributes[3][10]:
                    system("cls")
                    print("this national code is not valid")
                else:
                    for index, student in enumerate(students_list):
                        if student_nc == student[3]:
                            the_student_index = index
                            break

                    else:
                        system("cls")
                        input(
                            "ther is no student with national code {student_nc} in your list to delete.\npress enter to continue... "
                        )
                        system("cls")
                        break

                    if (
                        input(
                            f"Are you sure about deleting this student: {student[0]} {student[1]} {student[3]} {student[5]}\n(yes to remove, anythong else to cancel): "
                        )
                        == "yes"
                    ):
                        system("cls")
                        print(
                            "Notif: the student: ",
                            students_list.pop(the_student_index),
                            "\nhas been successfully removed",
                        )
                        break

                    else:
                        system("cls")
                        print("your request has been canceled")
                        break

        case "4":  # Search
            while True:
                search_choice = input(
                    "what do you want to use for searching? \n1- name\n2- family\n3- national code\n4- phone number\n\n(1-4 / cancel): "
                )
                main_search_choices = (0, 1, 3, 4)

                if search_choice == "cancel":
                    system("cls")
                    break

                if search_choice not in ("1", "2", "3", "4"):
                    system("cls")
                    print("your input was out of range (1, 2, 3, 4)")
                    continue

                search_phrase = input("enter the search phrase: ")

                for student in students_list:
                    if (
                        student[main_search_choices[int(search_choice) - 1]]
                        == search_phrase
                    ):
                        print(student)

                input("\npress enter to continue...")
                system("cls")

        case "5":  # Best score
            while True:
                bs_lesson_input = input(
                    "what lesson do you want to search the best score in? \n1- c_sharp\n2- java\n3- python\n\n(1-3 / cancel): "
                )
                system("cls")
                bs_lesson_indexes = (6, 7, 8)
                if bs_lesson_input == "cancel":
                    system("cls")
                    break

                elif bs_lesson_input not in ("1", "2", "3"):
                    print("pls enter a valid choice")
                    continue

                else:
                    highest_list = []
                    highest = 0
                    lesson_index = bs_lesson_indexes[int(bs_lesson_input) - 1]
                    for student in students_list:
                        if (val := student[lesson_index]) > highest:
                            highest_list = []
                            highest = student[lesson_index]
                            highest_list.append(student)

                        elif val == highest:
                            highest_list.append(student)

                    print(f"highest scores in {student_attributes[lesson_index][0]}: ")
                    for top_student in highest_list:
                        print(
                            top_student[0],
                            top_student[1],
                            top_student[3],
                            top_student[5],
                            top_student[2],
                            top_student[4],
                            top_student[int(bs_lesson_input) - 1],
                            sep=" - ",
                        )

                    input("\npress enter to continue... ")
                    system("cls")

        case _:
            print("pls enter a valid input")
