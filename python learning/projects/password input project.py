from os import system

system("cls")


while True:
    password = input("pls enter your password: ")
    main = password 
    specials = "!@#$%^&*_-"
    nums = "0123456789"
    system("cls")
    has_special = False
    has_nums = False
    

    password = password.strip()
    

    if len(password) < 8:
        system("cls")
        print("your password was smaller than 8 characters, pls try again")
        continue
        
    for each_special in specials:
        if each_special in password: # finding if it contains at least one of the specials
            has_special = True
            password = password.replace(each_special, "")
            
    if not has_special:
        system("cls")
        print(f"ther is no special character in you password: {", ".join(specials)}")
        continue

    for each_num in nums:
        if each_num in password: # finding if it contains at least one of the specials
            has_nums = True
            password = password.replace(each_num, "")
            
    if not has_nums:
        system("cls")
        print(f"ther is no number in you password: {", ".join(nums)}")
        continue
        
        
    if not len(password) > 0:
        system("cls")
        print("you have no alphabetic character in your password")
        continue
    
    if not password.isalpha(): # after removing all accepted special characters all thats remained should be alphabets and numbers
        system("cls")
        print("you have invalid characters in your password, pls enter another one")
        continue

    if password.isupper(): # checking if there is at least one lower case character
        system("cls")
        print("you should have at least one lowercase character in you password, pls enter another one")
        continue
    
    if password.islower(): # checking if there is at least one upper case character
        system("cls")
        print("you should have at least one uppercase character in you password, pls enter another one")
        continue

    print(f"that was a good password! so you password is: {main}")
    exit = input("do you wanna play again? (cancel to exit / anything else is continue): ")
    if exit == "cancel":
        break
    
            
