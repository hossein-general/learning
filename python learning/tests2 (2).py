from copy import copy, deepcopy
from os import system
system("cls")


# def function_name(data):
#     s = 0
#     for i in data:
#         s += i 
#     print(s)




# # test = [1,2,3,4]
# function_name()


# test = {"a":1, "b":2}
# sdf = {"sd", ("e", "f")}
# # print(type(**test))
# # test.update({"2": 2})
# test.update(sdf)



# print(test)
# print(type(test))
# # star-args in python (*test)
# # keyword-argsin python (**test)




# Concepts:
# type hint (var: type)


# def func(num1 = 12, num2 = 23, *num3, num4, num5 = "nothing", num6 = "nothing", **num7):
#     print("num1: ", num1)
#     print("num2: ", num2)
#     print("num3: ", num3)
#     print("num4: ", num4)
#     print("num5: ", num5)
#     print("num6: ", num6)
#     print("num7: ", num7)

    
# func(12,3,4,4,4,4,num4 = 2, num5 = 2, test = "te")
# func(1,2,3, 4, 5, num4 = 3, test = 2, ordr = 3, num6 = 3, num)




# def func(test):
#     test[0] = 13

# a = [1, 2, 3]

# print(a[0])
# func(a.copy())
# print(a[0])


# a = 14
# b = copy(a)

# a = ["Hossein", 9]
# b = a
# # b = copy(a)

# print(a is b)
# print(a == b)

# print(a)
# print(b)

# print()
# a[0] = "test"

# print(a)
# print(b)




# local - function
# global - module
# builting
# enclosing


# def func():
#     global num
#     print(num)
#     num = 13
#     del num

# num = 15
# func()
# print(num)






def func():
    def func2():
        def func3():
            global global_
            nonlocal local_1
            nonlocal local_2
            
            # nonlocal same
            
            global_ = 0
            local_1 = 1
            local_2 = 2
            # same = "its from function 3"
            print(global_)
            print(local_1)
            print(local_2)
            print(same)
            print("================")
            
        same = "its from function 2"
        local_2 = "lvl2"
        func3()
        print(local_2)
        print(same)
        
    same = "its from function 1"
    local_1 = "lvl1"
    func2()
    print(local_1)
    print(same)
    
same = "its from global"
global_ = "lvl0"
func()
print(global_)
print(same)



