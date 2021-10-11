# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
var_time_s =int(input("Введите количество секунд >>>"))
var_time_m = var_time_s//60
var_time_s = var_time_s%60
var_time_h = var_time_m//60
var_time_m = var_time_m%60
var_time_h = var_time_h%24
print(f'{var_time_h:02d}:{var_time_m:02d}:{var_time_s:02d}')