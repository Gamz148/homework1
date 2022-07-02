from os import mkdir
from os.path import join, exists


main_dir = "my_project_2"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp" ]
main_path = join(".", main_dir, main_dir)
if not exists(main_dir): mkdir(main_dir)
    # Можно было воспользоваться makedirs, у которого есть опция exist_ok
    # тогда не надо было бы проверять существование

for sub_dir in sub_dirs:
    sub_path = join(".", main_dir, sub_dir)
    if not exists(sub_path): mkdir(sub_path)
