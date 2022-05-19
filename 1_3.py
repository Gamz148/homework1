max_number = 101
first_number = 1
idx = 0

while idx < max_number:
    next_number = first_number + idx
    idx += 1
    #print(next_number)
    if next_number % 10 == 1 and next_number != 11: #and next_number == 1:
            print(next_number, 'процент')  #процент 1,21,31
    elif next_number % 10 == 2 and next_number != 12 or next_number % 10 == 3 and next_number != 13 or next_number % 10 == 4 and next_number != 14:
        print(next_number, 'процента')  #процента 2,3,4,22,23,24,32,33,34,
    else:
        print(next_number, 'процентов')    #процентов 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,35