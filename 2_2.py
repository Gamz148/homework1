list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия',
 'темп', 'воды', '+12', 'градусов', 'Цельсия']


# Создать новый список и наполнить его элементами по схеме:
#
# Обособить каждое целое число (исходного списка) кавычками
# (добавить элемент списка: строку-кавычку до и после элемента списка, являющегося числом)

# 1. Сколько проходов по исходному списку вам понадобится, чтобы сфор-
# мировать новый список? Достаточно одного прохода.

i = 0

while i < len(list_1):
    a = list_1[i]
    if a[-1].isdigit():
        list_1.insert(i, '"')
        i += 1
        str_len = 3 if a.startswith(('+', '-')) else 2
        if len(a) < str_len:
            a = a.zfill(str_len)
        i += 1
        list_1.insert(i, '"')
    i += 1
print(list_1)

def my_join(list_1):
    result = ''
    i = 0
    while i < len(list_1):
        a = list_1[i]
        if a == '"':
            a = ''.join(list_1[i:i+3])
            i += 2
        result = result + ' '
        i += 1
    return result
list_1 = my_join(list_1)
print(list_1)



i = 0

while i < len(list_2):
    a = list_2[i]
    if a[-1].isdigit():
        list_2.insert(i, '"')
        i += 1
        str_len = 3 if a.startswith(('+', '-')) else 2
        if len(a) < str_len:
            a = a.zfill(str_len)
        i += 1
        list_2.insert(i, '"')
    i += 1
print(list_2)

def my_join(list_2):
    result = ''
    i = 0
    while i < len(list_2):
        a = list_2[i]
        if a == '"':
            a = ''.join(list_2[i:i+3])
            i += 2
        result = result + ' '
        i += 1
    return result
list_2 = my_join(list_2)
print(list_2)