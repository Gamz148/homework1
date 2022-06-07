# from sys import getsizeof
#
# # Задача: пробежаться по большому списку чисел и вычислить сумму
# N = int(input('введите N: '))
# # Создаем список в памяти
# lst1 = [el for el in range(1,N+1,2)]
# print(f"Размер списка: {getsizeof(lst1)}")
# sum_num = 0
# for el in lst1:
#     sum_num += el
# print(f"Сумма: {sum_num}")
# #print(f"Список доступен после цикла for. Последний элемент {lst1[N]}")
# print(lst1)

from sys import getsizeof

N = int(input('введите N: '))
# Генераторные выражения
gen1 = (el for el in range(1,N+1,2))
#print(f"Размер генератора: {getsizeof(gen1)}")
# sum_num = 0
# for el in gen1:
#     sum_num += el
# print(f"Сумма: {sum_num}")
#print(f"Генератор недоступен после прохождения по нему. Исключение StopIteration")
for el in range(N):
    if next(gen1) < N:
        print(next(gen1))
    else:print('StopIteration')
