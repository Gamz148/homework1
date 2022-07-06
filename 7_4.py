from os import walk, stat
from os.path import join,abspath
from json import dumps

dir_name = "task_4_5"
root_dir = join(".", dir_name)
data_dir = join(root_dir, "some_data_adv")

size_bounds = [100,1000,10000,100000]

# Словарь создадим в одну строку
size_dict = {s: 0 for s in size_bounds}
for root, dirs, files in walk(data_dir):
    for file in files:
        file_size = stat(join(root, file)).st_size
        for size in size_dict.keys():
            if file_size <= size:
                size_dict[size] +=1
                break
print(size_dict)