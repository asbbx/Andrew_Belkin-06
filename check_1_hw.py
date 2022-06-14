# Подсчитать, сколько было выделено памяти под переменные в 
# ранее разработанных программах в рамках первых трех уроков. 
# Проанализировать результат и определить 
# программы с наиболее эффективным использованием памяти.

# Windows 10, Python - 3.9.10 x64

from check_byte import count_size


numbers = int(input('Введите число: '))

last_number = numbers % 10
second_number = numbers % 100 // 10
third_number = numbers // 100

sum_numbers = last_number + second_number + third_number
print(f"Сумма равна = {sum_numbers}")

multiplication_numbers = last_number * second_number * third_number
print(f"Произведение чисел =  {multiplication_numbers}")


variable_list = (numbers, last_number, second_number, third_number, sum_numbers, multiplication_numbers)
sum_variable = 0
for i in variable_list:
    sum_variable += count_size(i)
print(f'Под переменные выделено - {sum_variable} байт')

# Под переменные выделено - 156 байт
# 3 * 28 + 3 * 24 = 156 байт