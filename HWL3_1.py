#Реализовать функцию, принимающую два числа(позиционные аргументы) и
#выполняющую их деление.Числа запрашивать у пользователя, предусмотреть обработку
#ситуации деления на ноль.
a = input("Введите первое число : ")
b = input("Введите второе число : ")
def divon (x, y):
  if x.isdigit() and y.isdigit():
      x=float(x)
      y=float(y)
      try:
          print(f"Результат деления = {round(x/y,2)}")
      except ZeroDivisionError:
          print("Ошибка: Деление на 0")
  else:
      print("Один из аргументов строка! ")
divon(a,b)