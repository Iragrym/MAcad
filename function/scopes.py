

# def calc(num):
#     num2 =  num
#     return num2

# other_calc = calc


# print (other_calc(10))


# for i in range(1, 10):
#     if i == 1:
#         sm = 1
#     else:
#         sm += 1
# print(sm)


# def fun1():
#     def fun2():
#         def fun3():
#             pass

#         fun3()
#         fun2()
#         fun1()

#     fun2()
#     fun1()

# fun1()

number = 10
def func_outer():
    number = 10

    def func():
        nonlocal number
        number += 5

# func_outer()
# print(number)


def counter(start:int):
    value = start

    def next():
        nonlocal value
        value += 1
        return value

    return next

cntr = counter(0)
for _ in range(1, 30):
    print(cntr())
    



