from os import listdir, walk
from os.path import join
from shutil import copytree



root_dir = join(".", "task_3")
base_prj_dir = listdir(root_dir)[0]  # Считаем, что в корне - одна директория
templates_dir = join(root_dir, base_prj_dir, "templates")
for root, dirs, files in walk(root_dir):
    print(root, dirs, files)
    if "templates" in dirs:
        copytree(join(root,"templates"), templates_dir, dirs_exist_ok = True)