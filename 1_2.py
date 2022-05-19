numbers = []
for i in range(100):
    if i % 2 != 0:
        numbers. append(i**3)
print(numbers)

new_numbers = []
sum_num = 0
for num in numbers:
    i = num
    while num != 0:
        sum_num = sum_num + num % 10
        num = num // 10
    if sum_num % 7 == 0:
        new_numbers.append(i)
        sum_num = 0
print(sum(new_numbers))
