# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в текстовый файл.
# Проверить сохранённые данные.
# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
# При формировании словаря - хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# то для оставшихся ФИО использовать вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.

# Усложнение:
# Выполните запись результирующего словаря в файл json формата. Сделайте так чтобы русские букву читались
# как обычный текст, без преобразования в коды unicode.
# Примеры/Тесты:
#
# Фрагмент файла с данными о пользователях (task_3_users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Сидоров,Сидор,Сидорович
#
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
#
# скалолазание,охота
# горные лыжи
# вышивание крестиком, бои без правил
#
# Фрагмент результирующего файла (task_3_rezult.txt):
# {'ИИИ': 'скалолазание;охота', 'ППП': 'горные лыжи', 'ССС': 'вышивание крестиком; бои без правил'}


# file_1 = open('task_3_hobby.csv', 'r', encoding='utf-8')
# content = file_1.read()
# print(content)
# file_1.close()
#
# file_2 = open('task_3_users.csv', 'r', encoding='utf-8')
# content = file_2.read()
# print(content)
# file_2.close()
#
# file_3 = open('task_3_rezult.txt', 'a+', encoding='utf-8')
#
# print(content)
# file_3.close()

# with open ('task_3_users.csv', 'r', encoding='utf-8') as file_1:
#     for line1 in file_1:
#         print(line1)
#     with open('task_3_hobby.csv', 'r', encoding='utf-8') as file_2:
#         for line2 in file_2:
#             print(line2)
#         with open('task_3_rezult.txt', 'a+', encoding='utf-8') as f:
#             f.write(line1 + line2)



def initials(fio):
    """
    :param fio: массив строк вида ["Фамилия","Имя","Отчество"]
    :return: строка инициалов ФИО
    """
    fio = fio.strip().split(",")
    return "".join([fio[0][0], fio[1][0], fio[2][0]])

with open("task_3_users.csv",encoding="UTF-8", mode="rt") as file_fio:
    fio_data = file_fio.readlines()
with open("task_3_hobby.csv",encoding="UTF-8", mode="rt") as file_hobby:
    hobby_data = file_hobby.readlines()

fio_data_len = len(fio_data)
hobby_data_len = len(hobby_data)
dict_man3 = {}

# Запишем все в один цикл, используем максимум из двух длин
# тогда придется делать проверки:
# Индекс выйдет за пределы какого списка
for idx in range(max(fio_data_len, hobby_data_len)):
    if idx > fio_data_len-1:
        exit(1)
    if idx > hobby_data_len-1:
        value = None
    else:
        value = hobby_data[idx].strip().replace(",",";")
    fio = fio_data[idx]
    dict_man3[initials(fio)] = value


print(dict_man3)
# Сериализацию в Json никто не требовал
with open("task_3_rezult.txt",encoding="UTF-8", mode="wt") as file_out:
    file_out.write(str(dict_man3))
