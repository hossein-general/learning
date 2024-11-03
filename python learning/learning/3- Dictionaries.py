# dictionary:
#     is iterable
#     is mutable
#     not sequence
# Only Hashable types are accepted as keys
# -----------------

# ==============================={Setting}===============================
# ---------{empty Dictionary}---------
# data = dict()
# data = {}
# -----------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# data = {(i**2 if i%2 ==1 else i**3): ("even" if i%2 == 0 else "odd") for i in range(1, 101)}
# data["name"] = "mina"
# data["score"] = 24.3
# print(data)

# -------------------------------------------------------------------------

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# data.setdefault("name")
# data.setdefault("score")      # adds None as a default value if the score wasnt found
# data.setdefault("score", "0") # uses 0 to define a new variable

# print(data)

# -------------------------------------------------------------------------

# data2 = {"name": "meisam", "family": "ilka", "score": 34}
# data = ('name', 'family', 'age')
# data = ['name', 'family', 'age']

# res = data2.fromkeys(data, "") # using an iterable and a default value to create a dictionary
# res = dict.fromkeys(data, "") # using an iterable and a default value to create a dictionary

# print(data2 )
# print(res)

# ==============================={Getting}===============================

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
# data.update((("name", "tahere"), ("score", 34)))
# data.update([("name", "tahere"), ("score", 34)])
# data.update(name="taere", score=34)
# data.update({"name": "tahere", "score": 34}, name="taere", score=34)
# data.update((("name", "tahere"), ("score", 34)), name="taere", score=34)
# data.update([("name", "tahere"), ("score", 34)], name="taere", score=34)

# print(data)

# ---------------[in]---------------
# data = {"name": "meisam", "family": "Ramezani", "age": 34}


# res = "name" in data
# res = ("name", "family") in data    # this one looks for a tuple inside the dictionary KEYS no each value one by one
# res = ["name", "family"] in data    # Unhashable type error
# res = {"name", "family"} in data    # Unhashable type error
# res = {"name": "meisam", "family": "Ramezani"} in data # Unhashable type error
# print(res)

# -------------------------------------


# ==============================={Views}===============================

# data = {"name": "meisam", "family": "Ramezani", "age": 34}

# res = data.keys()
# # res = data.values()
# # res = data.items()

# print(type(res))
# print(res)

# data["score"] = 33

# print(res)

