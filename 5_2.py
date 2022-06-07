# Написать генератор нечётных чисел от 1 до n (включительно),
# используя ключевое слово yield. Полностью истощить генератор.


def iterator_yield(N):
    for i in range(1, N+1, 2):
        yield i

s = iterator_yield(10)
#print(list(s))
print(next(s))
print(next(s))
print(list(s))
print(next(s))


def iterator_yield_1(N):
    for i in range(1, N+1, 2):
        if i**2 < 200:
            yield i

s = iterator_yield_1(100)
#print(list(s))
print(next(s))
print(next(s))
print(list(s))
print(next(s))