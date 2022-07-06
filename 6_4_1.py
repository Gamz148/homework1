
from sys import argv

if len(argv)<2:
    print("Не передана сумма продаж")
    exit(1)

with open("bakery.csv", encoding="UTF-8", mode="at") as file:
    file.write(f"{argv[1]:>5s}\n")
