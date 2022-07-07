# set

# set1 = {1, 'Ulan', 3, (1, 2), 4, 1}
# print(set1)
#
# set1 = set()
# # set1 = {}
# print(type(set1))

# set1 = {"Monday", "Thuesday", "Wednesday"}
# for i in set1:
#     for j in i:
#
#         print(j)

# union()

# set1 = {"Monday", "Thuesday", "Wednesday", "Saturday"}
# set2 = {"Saturday", "Friday", "Monday"}
# # s = set1.difference(set2)
# set1 = set1.difference_update(set2)
# print(set1)
# print(set3)
# print(s)
# s = set1.union({"Saturday", "Friday"})
# s = set1.union(set2)
# set1.add("Saturday")
# set1.clear()
# difference



# print(set1.difference(set2))

# print(set2.symmetric_difference_update(set1))
# print(set2)


# str1 = {"a", "b", "c"}
# str2 = {"a", "b", "d"}
# pop_set = str2.pop()
# print(pop_set)
# print(str2)
# str_set = str1.difference(str2)
# print(str_set)
# str2.discard("a")
# str2.remove("p")
# print(str2)

a = [1, 2, 3, 4, 6, 8, 7, 9, 9]
b = [1, 6, 7, 9]
a1 = set(a)
b1 = set(b)
# print(a1.issubset(b1))
# set5 = a1.symmetric_difference(b1)
# set6 = a1.symmetric_difference_update(b1)
# print(a1)
# print(b1)
# a1 = list(a1)
# print(a1)
# print(a1.intersection(b1))
# a1.intersection_update(b1)
# print(a1)
# print(a1.issubset(b1))

print(a1.issuperset(b1))


