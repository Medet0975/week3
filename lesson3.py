# function

# def test_func():
#     print("Hello world")
# test_func()

# def test_func():
#     pass

# summ = int(input('enter a sum: '))
# year = int(input('enter a period: '))
# percent = float(input('percent: '))
# percent_for_year = summ * percent
# all_cash = percent_for_year * year + summ
# print(all_cash)

# def get_cash(summ, year, percent):
#     all_cash = int(summ * ((percent+1) ** year))
#     print(all_cash)
#     return all_cash
# get_cash(summ, year, percent)

# cash = int(get_cash(100, 3))
# # print(get_cash(100, 3)
#
# # get_cash(500000, 5, 0.2)
# # get_cash(300000, 5, 0.2)
# print(get_cash)
# get_cash()

# from random import randint
# num = int(input("enter a number:   "))
# for i in range(num):
#     # if randint(0,9) > 0:
#     print(randint(0,9), end = "")

# from random import randint
# num = int(input("enter a number:   "))
# for i in range(num):
#     a = randint(0,9)
#     if a == 0
#     print(a, end = "")

# from random import randint
# num = int(input("enter a number:   "))
# min = 10 ** (num-1)
# max = 10 ** (num)
# if num == 1:
#     min = 0
# print(randint(min, max))

# lists = []
# lists = [i for i in range(min, max)]
# print(lists)

# lists = []
# tik_tak = [["o", 0, "x"], [0, 0, "x"], ["x", 0, "o"]]
# print(len(tik_tak))
# print(len(tik_tak[1]))
# for i in range(len(tik_tak)):
#     for j in range(len(tik_tak[i])):
#         print(j)
#         if tik_tak[i][j] == 0:
#             lists.append([i, j])
# print(lists)
# m = int(input())
# n = int(input())
def bank(m, n):
    all_cash = int(m * (1.1 ** n))
    print(all_cash)
    return all_cash
bank(m=100, n=3)