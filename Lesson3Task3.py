# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return 'Вводите только числа!'


print(my_func(10, 10, 2))

# Через варианты
def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg2 and arg3 >= arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3

print \
    (f'Result - {my_func(int(input("Enter 1st argument: ")), int(input("Enter 2nd argument: ")), int(input("Enter 3rd argument: ")))}')

# Вариант
def my_func(x, y, z):
    if x < y:
        x, y = y, x
    if y < z:
        y, z = z, y
    return int(x) + int(y)


print(my_func(input(), input(), input()))

# Вариант
from heapq import nlargest


def sum_of_max(a, b, c):
    n = sum(nlargest(2, [a, b, c]))
    print(f'Сумма двух наибольших из введенных вами чисел =', n)


sum_of_max(3, 4, 2)


