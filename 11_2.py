
class CheckZeroDivision(ZeroDivisionError): pass


def divide(num, denom):
    try:
        return num/denom
    except ZeroDivisionError:
        raise CheckZeroDivision(f"Деление {num} на {denom} запрещено!")


try:
    print(divide(15,1))
    print(divide(14,0))
except CheckZeroDivision as err:
    print(err)

