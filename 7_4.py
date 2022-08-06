import os
from os import mkdir
from os.path import join, exists
import shutil
import random
from os import walk, stat
from os.path import join,abspath
from json import dumps


folder = (r'C:\Users\Олег\PycharmProjects\DZ_7_1')
print(os.getcwd()) # проверка месоположения

#создать иерархию папок
dir_path = r'task_4\my_project'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Создадим в папке task_4\my_project 100 небольших файлов разного размера.
folder = 'task_4\my_project'
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 2):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255)
        for _ in range(random.randrange(10 ** 5)))
    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)

# границы диапазонов размеров файлов
size_bounds = [100,1000,10000,100000]

# Словарь создадим в одну строку
size_dict = {s: 0 for s in size_bounds}
for dir_path, files in walk(folder):
    for file in files:
        file_size = stat(join(folder, file)).st_size
        for size in size_dict.keys():
            if file_size <= size:
                size_dict[size] +=1
                break  # Подумайте почему break обязателен
print(size_dict)
