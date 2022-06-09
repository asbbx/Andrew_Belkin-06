from check_byte import count_size


x1 = float(input('Введите координаты x1 '))
y1 = float(input('Введите координаты y1 '))
x2 = float(input('Введите координаты x2 '))
y2 = float(input('Введите координаты y2 '))
if x1 != x2:
    i = (y2 - y1)/(x2 - x1)
    j = (x2*y1 - x1*y2)/(x2 - x1)
    print(f'Уравнение прямой y = {i}x + {j}')
else:
    print(f'Уравнение прямой x = {x1}')

our_list = (x1, y1, x2, y2, i, j)
sum_variable = 0
for i in our_list:
    sum_variable += count_size(i)
print(f'На переменные затрачено {sum_variable} байт')
# На переменные затрачено 144 байт
