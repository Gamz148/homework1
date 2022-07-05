import os



def parse_yaml_string(src_string, space = 2):

    lst_yaml_string = src_string.split("-")
    name = lst_yaml_string[-1].strip(" \n")

    if name[-1] == ":":
        isfile = False
        name = name[:-1]
    else:
        isfile = True
    lenght = len(lst_yaml_string)

    if lenght > 1:
        level = len(lst_yaml_string[0]) // space
    else:
        level = 0
    return level, name, isfile

prefix_name = "task_7_2"
yaml_path = os.path.join(".", prefix_name, "config_2.yaml")
current_path = []
current_level = -1
with open(yaml_path, encoding="UTF-8", mode = "rt") as file:
    for line in file:
        level, name, isfile = parse_yaml_string(line)

        if current_level < level:

            current_path.append(name)
            current_level += 1
        elif current_level == level:

            current_path[-1] = name
        else:

            for i in range(current_level-level+1):
                current_path.pop()
                current_level -= 1
            current_level += 1
            current_path.append(name)

        dir_path =  os.path.join(".",prefix_name,*current_path)
        if not os.path.exists(dir_path):
            if isfile:
                # Этот код для windows, Unix системы можно исполозвать mknod
                with open(dir_path, encoding= "UTF-8", mode = "w"):
                    pass
            else:
                os.makedirs(dir_path)
