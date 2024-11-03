# Set is a collection of Keys
# Only Hashable types are accepted

# supported functions and operations and otehrs:
# len()
# in
# id()
# ...


# ==============================={Set}===============================
# ---------{empty set}---------
# data = set()
# -----------------------------

# data = {"meisam", "ilka", 31}
# test = {(i, "even") if i % 2 == 0 else (i, "odd") for i in range(1, 100)}
# data = set((i, "even") if i % 2 == 0 else (i, "odd") for i in range(1, 100))
# print(data)

# ----------------------------------------------------

# data = {2, 3, 4}

# data.add(30)
# print(data)

# ==============================={Get}===============================
# data = {2, 3, 4}

# for item in data:
#     print(item)

# ==============================={Copy}===============================
# data = {"meisam", "ilka", 31}
# new_data = data
# new_data = data.copy()

# print(new_data)


# ==============================={Comparision and Relational Methods}===============================
data1 = {2, 3, 4}
data2 = {4, 5, 6}
tuple_ = (4, 5, 6)
list_ = [4, 5, 6]
dict_ = {4: "four", 5: "five", 6: "six"}

# -------------------------------------------------------------------------------------------------------------------
# print(data1 == data2)
# print(data1 is data2)

# if no intersection / completely seperated---------------------------------------------------------------------------
# res = data1.isdisjoint(data2)
# res = data1.isdisjoint(tuple_)
# res = data1.isdisjoint(list_)
# res = data1.isdisjoint(dict_)
# print(res)

# if one is a subset of the other ------------------------------------------------------------------------------------
# res = data1.issubset(data2)
# res = data1.issubset(tuple_)
# res = data1.issubset(list_)
# res = data1.issubset(dict_)
# print(res)

# if one is a superset of the other ------------------------------------------------------------------------------------
# res = data1.issuperset(data2)
# res = data1.issuperset(tuple_)
# res = data1.issuperset(list_)
# res = data1.issuperset(dict_)
# print(res)

# Union (اجتماع) # Return a set containing the union of sets --------------------------------------------------------
# res = data1 | data2
# res = data1.union(data2)
# res = data1.union(tuple_)
# res = data1.union(list_)
# res = data1.union(dict_)
# print(res)
# ......................................................
# data1.update(data2)
# data1.update(tuple_)
# data1.update(list_)
# data1.update(dict_)
# print(data1)


# Intersection (اشتراک) # Returns a set, that is the intersection of two other sets ---------------------------------
# res = data1 & data2
# res = data1.intersection(data2)
# res = data1.intersection(tuple_)
# res = data1.intersection(list_)
# res = data1.intersection(dict_)
# print(res)
# ......................................................
# data1.intersection_update(data2)
# data1.intersection_update(tuple_)
# data1.intersection_update(list_)
# data1.intersection_update(dict_)
# print(data1)


# Union - Subscription  (اجتماع منهای اشتراکات) # Returns a set with the symmetric differences of two sets ---------
# res = data1 ^ data2
# res = data1.symmetric_difference(data2)
# res = data1.symmetric_difference(tuple_)
# res = data1.symmetric_difference(list_)
# res = data1.symmetric_difference(dict_)
# ......................................................
# data1.symmetric_difference_update(data2)
# data1.symmetric_difference_update(tuple_)
# data1.symmetric_difference_update(list_)
# data1.symmetric_difference_update(dict_)
# print(data1)


# Difference  (منهای) # Returns a set containing the difference between two or more sets ----------------------------
# res = data1 - data2
# res = data1.difference(data2)
# res = data1.difference(tuple_)
# res = data1.difference(list_)
# res = data1.difference(dict_)
# print(res)
# ......................................................
# data1.difference_update(data2)
# data1.difference_update(tuple_)
# data1.difference_update(list_)
# data1.difference_update(dict_)
# print(data1)


# ==============================={Clear/Delete/Discarding}===============================
# data = {2, 3, 4}

# data.clear()
# print(data)

# -----------------------------------------
# data = {2, 3, 4}

# data.discard(3) # no error in case of value not existing
# print(data)

# -----------------------------------------
# data = {2, 3, 4}

# data.remove(3) # error if value doesnt exist (KeyError)
# print(data)

# -----------------------------------------
# data = {2, 3, 4}

# res = data.pop()
# print(res)
# print(data)
