list_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# i = 0
# idx = 0
# for i in list_1:
#     while idx < len(list_1):
#         print('привет ', i)
#         idx += 1

# for el in list_1:
#     name = el.split()[-1].capitalize()
#     print(f'Привет, {name}!')


for element in list_1:
    name = element.split()[-1]
    e = name.capitalize()
    #print(name)
    print('Привет,', e)