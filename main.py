def calculator(temp):
    elem = temp.split(" ")

    a = int(elem[0])
    b = int(elem[2])

    if a <= 10 and b <= 10:

        if len(elem) == 3:

            if elem[1] == "+":
                return plus(a, b)

            elif elem[1] == "-":
                return minus(a, b)

            elif elem[1] == "*":
                return multiply(a, b)

            elif elem[1] == "/":
                return division(a, b)

            else:
                return print("строка не является математической операцией")

        else:
            return print("формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)")

    else:
        print("Неверный формат!")


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

