""" def say_hello(name: str) -> None:
    print('Hello,', name)


def my_func(*pos_params, a, b, c, d,):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)
    print('pos = ', pos_params)

my_func(1, 2, 3, 4, b=1, a=2, d=3, c=4,)

say_hello('Misha')
say_hello('Slavik')
say_hello('Illa') """


import os


def my_print(*values, sep=' ', end='\n'):
    value_ls = list(str(val) for val in values)
    out = sep.join(value_ls)
    return f'{out}{end}'

out = my_print(1, 2, 3, 4, sep='<>', end='\n\n\n')
out = my_print([1, 2, 2, 3, 34])
out = my_print('a, b, c')

    #for value in values:





