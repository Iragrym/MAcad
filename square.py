""" import math

a = 10
b = 12
c = 20

if (a+b>c) and (a+c>b) and (c+b>a):
    p = (a+b+c)/2
    S = math.sqrt(
        p*(p-a)*(p-b)*(p-c)
    )
    print('Площадь равна:', round(S, 5))
else:
    print('Треугольник не существует')
 """

