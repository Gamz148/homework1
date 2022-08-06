
import os
from os import mkdir
from os.path import join, exists

# удалить всю структуру папок
import shutil
# shutil.rmtree('my_project')
# shutil.rmtree('task_1')



folder = (r'C:\Users\Олег\PycharmProjects\DZ_7_1')
print(os.getcwd()) # проверка месоположения

# first_dir = 'task_1' # создание папки
# if not os.path.exists(first_dir):
#     os.mkdir(first_dir)

#создать иерархию папок
dir_path = r'task_1\my_project'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

first_dir = 'task_1'
main_dir = 'my_project'
sub_dirs = ["settings", "mainapp", "adminapp", "authapp" ]
main_path = join(".",first_dir, main_dir)
if not exists(main_path): mkdir(main_path)

for sub_dir in sub_dirs:
    sub_path = join(".",first_dir, main_dir, sub_dir)
    if not exists(sub_path): mkdir(sub_path)
