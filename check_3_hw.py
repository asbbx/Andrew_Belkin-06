from check_byte import count_size

our_number = int(input('Введите число: '))
counter_even = 0
counter_odd = 0
while our_number > 0:
    if our_number % 2 == 0:
        counter_even += 1
    else:
        counter_odd += 1
    our_number //= 10

print(f'Четных: {counter_even} Нечетных: {counter_odd}')

our_list = (our_number, counter_even, counter_even, our_number)
sum_variable = 0
for i in our_list:
    sum_variable += count_size(i)
print(f'На переменные затрачено {sum_variable} байт.')

# На переменные затрачено 96 байт.
