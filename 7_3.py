
import os
from os import mkdir
from os.path import join, exists
import shutil


folder = (r'C:\Users\Олег\PycharmProjects\DZ_7_1')
print(os.getcwd()) # проверка месоположения

#создать иерархию папок
dir_path = r'task_3\my_project'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

first_dir = 'task_3'
main_dir = 'my_project'
main_dir1 = 'templates'
sub_dirs = ["mainapp","authapp"]

main_path = join(".",first_dir, main_dir,"..",main_dir1)
if not exists(main_path): mkdir(main_path)

for sub_dir in sub_dirs:
    sub_path = join(".",first_dir,main_dir,"..",main_dir1, sub_dir)
    if not exists(sub_path): mkdir(sub_path)

#добавление файлов html
file1 = open('base.html', 'wt')
print('Oops, I created a file.', file=file1)
file1.close()
file2 = open('index.html', 'wt')
print('created a file2.', file=file2)
file2.close()

file1 = open('base.html', 'wt')
print('Oops, I created a file.', file=file1)
file1.close()
file2 = open('index.html', 'wt')
print('created a file2.', file=file2)
file2.close()

# перемещение файлов
shutil.move('base.html', 'task_3/templates/authapp')
shutil.move('index.html', 'task_3/templates/authapp')
