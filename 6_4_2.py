from sys import argv


def show_lines(file, begin = None, end = None):
    for idx, line in enumerate(file):
        is_begin_norm = (begin is not None and idx >= begin-1) or begin is None
        is_end_norm = (end is not None and idx <= end-1) or end is None
        if is_begin_norm and is_end_norm:
            print(line.strip())

# argv = ["bla-bla-bla"]
# argv = ["bla-bla-bla",1]
argv = ["bla-bla-bla",1,3]
len_argv = len(argv)


with open("bakery.csv", encoding="UTF-8", mode="rt") as file:
    if len_argv == 1:
        print("Show all records:")
        show_lines(file, begin = None, end = None)
    elif len_argv == 2:
        record_begin = int(argv[1])
        print(f"Show records from record {record_begin}:")
        show_lines(file, begin = record_begin, end = None)
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])
        print(f"Show records from record {record_begin} to record {record_end}")
        show_lines(file, begin = record_begin, end = record_end)