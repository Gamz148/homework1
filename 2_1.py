# 1. Выяснить тип результата следующих выражений:
#
#     15 * 3
#     15 / 3
#     15 // 2
#     15 ** 2
#
# Техническое задание:
#
#     Вывести на экран тип выражения и отдельно проверить является ли полученный тип
#     целым числом.

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

list = [a, b, c, d]

for i in list:
    if type(i) == int:
        print(i, 'целое число')
    else:
        print(i, 'число не целое!')