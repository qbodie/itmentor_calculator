def calculator(temp):
    elem = temp.split(" ")

    if len(elem) == 3:

        if elem[1] == "+":
            return plus(elem[0], elem[2])

        elif elem[1] == "-":
            return minus(elem[0], elem[2])

        elif elem[1] == "*":
            return multiply(elem[0], elem[2])

        elif elem[1] == "/":
            return division(elem[0], elem[2])

        else:
            return print("строка не является математической операцией")

    else:
        return print("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")


def plus(a, b):
    return print(int(a) + int(b))


def minus(a, b):
    return print(int(a) - int(b))


def multiply(a, b):

    return print(int(a) * int(b))


def division(a, b):

    if b != "0":
        return print(int(a) / int(b))

    return print("Делить на ноль нельзя!")


if __name__ == "__main__":
    line = input("Введите пример: ")
    calculator(line)

