import os

prefix_name = "task_7_1"
main_dir = "my_project1"
sub_dirs = ["settings", "mainapp", "adminapp", "authapp" ]
main_path = os.path.join(".", prefix_name, main_dir)
if not os.path.exists(main_path): os.mkdir(main_path)


for sub_dir in sub_dirs:
    sub_path = os.path.join(".", prefix_name, main_dir, sub_dir)
    if not os.path.exists(sub_path): os.mkdir(sub_path)
