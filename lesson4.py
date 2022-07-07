# shop_cash = [10000, 34000, 30000, 12300, 45000, 90000, 78999]
# expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
# shop_cash2 = [10000, 34000, 30000, 12300, 45000, 90000, 78999]
# expenses2 = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
#
#
# # all_cash = sum(shop_cash)
# # all_expenses = sum(expenses)
# # profit = all_cash - all_expenses
# # print(profit)
# def get_money(shop_cash : list, expenses : list):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit
# monday = get_money(expenses=expenses2, shop_cash=shop_cash2)
# day2 = get_money(shop_cash2, expenses2)
# print(monday)


# *args ** kwargs

# def get_arguments(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
# get_arguments(1, 2, 3, "dffgg", {1, 0}, name ='Nazgul', age =

# d = {
#     "name": "Nazgul",
#
# }

def get_list_square(*args, **kwargs):
    result = []
    # kwargs ={}
    if args:
        for i in args:
            result.append((i**2))
    if kwargs:
        for key, value in kwargs.items():
            if type(value) == str:
                kwargs.update({
                    key: value.upper()
                    })
            if type(value) == set:
                kwargs.update({
                    key: [value]
                    })
            # if type(valey) == str:
            #     dicts.update({
            #         key: value.upper()
            #         })
    return result, kwargs
print(get_list_square(1, 3, 7, 11, name="Nazi", age=50, sets={1,3}))