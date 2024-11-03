from os import system

system("cls")

# tup1 = ("name", "family", "age", "score")
# tup2 = ("Hossein", "Ramezani", 34, (1.2, 1.4))

# tup3 = (("name", "Hossein"), ("family", "Ramezani"), ("age", 34), ("score", (1.2, 1.4)))
# tup4 = [["name", "Hossein"], ("family", "Ramezani"), ["age", 34], ("score", (1.2, 1.4))]


# val = zip(tup2, tup1)

# # for i in val:
# #     print(i)


# testing1 = dict([["name", "Hossein"], ["family", "Ramezani"], ["age", 34], ["score", (1.2, 1.4)]])

# print(testing1)
# print()

# # testing1.clear()
# testing1.
# print(testing1)
# print(type(testing1))


# # testing1 = dict(val, test="testing")

# # print(testing1)

# # val = zip(tup1, tup2)
# # testing2 = dict(val)

# # print(testing2)


# # test1 = dict()
# # test2 = dict(name="Hossein", family="Ramezani", age=34, score=1.2)
# # test3 = {"name":"Hossein", "family":"Ramezani", "age":34, "score":1.2}
# # test4 = dict()

# # print("test1 - type: ", type(test1), "\t", test1)
# # print("test2 - type: ", type(test2), "\t", test2)
# # print("test3 - type: ", type(test3), "\t", test3)
# # print("test4 - type: ", type(test4), "\t", test4)


# data = {"name":"meisam", "family":"Ramezani", "age":34}

# res = "name" in data

# -------------------------------------------------------------------------

# data1 = {"name": "meisam", "family": "Ramezani", "age": 34}
# data2 = {"family": "Ramezani", "age": 34, "name": "meisam"}

# print(data1 == data2)

# -------------------------------------------------------------------------

# data1 = {"name": "meisam", "family": "Ramezani", "age": 34}
# data2 = {"family": "Ramezani", "age": 34, "name": "meisam"}

# print(data1 == data2)
# print(id(data1))
# print(id(data2))
# print(data1 is data2)

# .......................................

# data1 = {"name": "meisam", "family": "Ramezani", "age": 34}
# data2 = data1

# print(data1 == data2)
# print(id(data1))
# print(id(data2))
# print(data1 is data2)

# .......................................

# data1 = {"name": "meisam", "family": "Ramezani", "age": 34}
# data2 = data1.copy()

# print(data1 == data2)
# print(id(data1))
# print(id(data2))
# print(data1 is data2)

# ==============================={Getting}===============================
# dictionary:
#     is iterable
#     is mutable
#     not sequence
# -----------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# val = data["name"]
# val = data["score"] # KeyError
# print(val)

# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# val = data.get("name")
# val = data.get("score")
# val = data.get("score", "the key wasnt found!")
# print(val)

# ==============================={Setting}===============================

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# data["name"] = "mina"
# data["score"] = 24.3
# print(data)


# -------------------------------------------------------------------------

# data = {(i**2 if i%2 ==1 else i**3): ("even" if i%2 == 0 else "odd") for i in range(1, 101)}

# print(data)


# ==============================={Clearing/Deleting}===============================

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# data.clear()
# print(data)


# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# del data["nmae"]
# del data
# print(data)


# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# res = data.pop("name")
# res = data.pop("score")
# res = data.pop("score", "the score doesnt exist!")
# print(res)


# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# res = data.popitem() # dont concider sequence
# print(res)


# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# res = data.popitem() # dont concider sequence
# print(res)


# ==============================={Update}===============================

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# data.update({"name": "tahere", "score": 34})


# -------------------------------------------------------------------------


data = {"name": "meisam", "family": "Ramezani", "age": 34}

res = "name" in data
print(res)
