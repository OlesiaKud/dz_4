# 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.
n = int(input('Введите кол-во элементов первого множества:'))
m = int(input('Введите кол-во элементов второго множества:'))
n1 = []
m1 = []
res_list = []

print('Введите первое множество.')
for i in range (n):
    val_n = int(input(f'Введите {i + 1} элемент: '))
    n1.append(val_n)
print('Введите второе множество.')
for j in range (m):
    val_m = int(input(f'Введите {j + 1} элемент: '))
    m1.append(val_m)

res_list = n1 + m1
print('Числа, которые встречаются в заданных двух множетсвах:')
print(set(sorted(res_list)))