# set1 = {
#     1, 2, 3, 4, 5
# }
# set2 = {1, 2, 3, 4, 5, 4, 6}
# set1 = {"Hello", "banana"}
# set2 = {"Hello", "apple", "pineapple"}
# set3 = {"Hello", "potato", "orange"}
# print(set1.union(set2))
# set1.update(set2)
# print(set1)
# print(set1.isdisjoint(set2))
# print(set1.intersection(set3, set2))

# a1 = {1, 2}
# a2 ={3}
# a3 ={4, 5}
# a4 = {3, 2, 6}
# a5 = {1, 2}
# a6 = {7, 8}
# a7 = {9,8}
# print(a1.intersection(a2, a3, a4, a5, a6, a7))
# for i in range(2, 8, 1):
#     dis = a1.isdisjoint(f'a"{i}"')
#     print(dis)
    # a8 = a1.intersection(ai)
    # print(a8)

# set1 = {"set", "5", "2", "6"}
# set2 = {"3", "5", "2", "6"}
# print(set1.issuperset(set2))
# if set1.issuperset(set2) and set2.issuperset(set1):
#     print("это супермножество")
# else:
#     print("Супермножество не обнарyжено")
# if set1 == set2:
#     print("они равны")

# # comprehension - lists, dict
# lists = []
# for i in range(0,10001, 10):
#     lists.append(i)
# print(lists)

# lists = [i for i in range(1, 10001)]
# print(lists)

# str1 = "ddfsdfjskdfjskjalkjlkajgaaggkjagalglagkal"
# lists2 = [i for i in str1]
# print(lists2)


import datetime

# time_now = datetime.datetime.now()
# print(time_now)

# lists = []
# time_now = datetime.datetime.now()
# for i in range(1,10000):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)

time_now = datetime.datetime.now()
lists = [i**2 for i in range(1, 10001) if i % 20 == 0 and i % 5 == 0]
delta = datetime.datetime.now() - time_now

print(lists)
print(delta)
# time_now = datetime.datetime.now()
# num = int(input())
# fact = 1
# for num1 in range(1, num+1):
#     s = 2 * num1
#     print(s)
#     # fact = fact * num1
#
#     # print(num1)
# # print(fact)
# delta = datetime.datetime.now() - time_now
# print(delta)

# dicts = {i: i*(i+1) for i in range(1,5)}
# print(dicts)


# lists = ['apple', 'banana', 'orange', 'lemon', 'cherry']
# dicts ={i: i for i in lists}
# for i in range(1, 5):
# for j in range(0,5):
#     s = lists[j]
# dicts = {lists[1]: i for i in lists}
# print(s)
# print(dicts)
# from random import randint
# lists = ['rock', 'paper', 'scissors']
# name = str(input("enter a name: "))
# while True:

#     print(turn1)

#     print(comp)
# i = 0
# j = 0
# for i in range(1, 3):


# while i<3 and j<3:
#     turn1 = str(input('enter your turn: '))
#     comp = lists[randint(0, 2)]
#     print("Laptop: ", comp)
#     if turn1 == lists[0] and comp == lists[2]:
#         i += 1
#         print('you win')
#     elif turn1 == lists[1] and comp == lists[0]:
#         i += 1
#         print('you win')
#     elif turn1 == lists[2] and comp == lists[1]:
#         i += 1
#         print('you win')
#     elif turn1 == comp:
#         i += 0
#         print("draw")
#     else:
#         j += 1
#         print("you loser")
#     print(i, "-", j)






