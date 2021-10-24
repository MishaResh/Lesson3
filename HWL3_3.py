# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
var1 = input("Введите 1-ый аргумент : ")
var2 = input("Введите 2-ой аргумент : ")
var3 = input("Введите 3-ий аргумент : ")


def my_func(x, y, z):
    if x.isdigit() and y.isdigit() and z.isdigit():
        x, y, z = float(x), float(y), float(z)
    list = [x, y, z]
    list.sort()
    return list[2] + list[1]


print(f'Сумма двух наибольшех чисел = {my_func(var1, var2, var3)}')
