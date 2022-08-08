# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера `nginx_logs.txt`
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# получить список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)`. Например:
# ```
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# ```
# Примечание:**
# - код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# - Вы не знате заранее насколько точно идентичны строки файла. Попробуйте оценить это. Возможно вам помогут множества.

list_string = []
with open("log.txt", encoding="UTF-8", mode="rt") as file:
    for line in file:
        line1, line2, *_ = line.split('"')
        line1, line2 = line1.split(), line2.split()
        list_string.append((line1[0], line2[0], line2[1]))

for el in list_string:
    print(el)
    