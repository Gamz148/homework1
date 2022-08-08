
class NotNumberException(Exception): pass

def prepared_data(data):
    try:
        return  float(data)
    except ValueError:
        raise NotNumberException(f"{data} - не  число")

lst = []
while True:
    line = input("Введите данные. Для остановки введите 'stop' ")
    if line == "stop":
        break
    try:
        lst.append(prepared_data(line))
    except NotNumberException as err:
        print(err)
        continue

print(lst)
