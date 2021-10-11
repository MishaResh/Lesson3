# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
var_ch = int(input("Введите число >>> "))
max_ch = 0
while var_ch > 0:
    max_ch1 = var_ch % 10
    if max_ch1 > max_ch:
        max_ch = max_ch1
    var_ch = var_ch // 10
print(max_ch)
