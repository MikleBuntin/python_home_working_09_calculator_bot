

def literals_controle(numbers):
    numbers = numbers.replace('.', '')
    numbers = numbers.replace(',', '')
    numbers = numbers.replace('+', '')
    numbers = numbers.replace('-', '')
    numbers = numbers.replace('*', '')
    numbers = numbers.replace('/', '')
    return numbers.isdigit()
def text_to_float(numbers):
    # print("3: ", numbers)
    # print(type(numbers[0]))
    if str(numbers[0]).find('.') > 0:
        numbers[0] = float(numbers[0])
    elif str(numbers[0]).find(',') > 0:
        numbers[0] = float(numbers[0].replace(',', '.'))
    elif str(numbers[0]).isdigit():
        numbers[0] = int(numbers[0])
    else:
        return "Недопустимый символ"


    if str(numbers[1]).find('.') > 0:
        numbers[1] = float(numbers[1])
    elif str(numbers[1]).find(',') > 0:
        numbers[1] = float(numbers[1].replace(',', '.'))
    elif str(numbers[1]).isdigit():
        numbers[1] = int(numbers[1])
    else:
        return "Недопустимый символ"

    return numbers


def input(message):
    message = message.replace(' ', '')
    if literals_controle(message):
        if message.find('+') > 0:
            if len(message.split('+')) == 2:
                return str(summ(message.split('+')))
            else:
                return "Можно сложить только два числа."


        elif message.find('-') > 0:
            if len(message.split('-')) == 2:
                return str(diff(message.split('-')))
            else:
                return "Можно задать только два числа."

        elif message.find('*') > 0:
            if len(message.split('*')) == 2:
                return str(mult(message.split('*')))
            else:
                return "Можно перемножить только два числа."

        elif message.find('/') > 0:
            message = message.split('/')
            if len(message) == 2:
                if message[1] == '0':
                    return "У нас делить на ноль нельзя. Пока нельзя :)"
                else:
                    return str(div(message))
            else:
                return "Числа должно быть два."

        else:
            return "Не могу понять что считать.."
    else:
        return "Сегодня работаем только с цифрами."


def summ(numbers):

    if numbers[0].isdigit() and numbers[1].isdigit():
        return int(numbers[0]) + int(numbers[1])
    else:
        if type(text_to_float(numbers)) == "str":
            return text_to_float(numbers)
        else:
            numbers = text_to_float(numbers)
            return numbers[0] + numbers[1]

def diff(numbers):
    if numbers[0].isdigit() and numbers[1].isdigit():
        return int(numbers[0]) - int(numbers[1])
    else:
        if type(text_to_float(numbers)) == "str":
            return text_to_float(numbers)
        else:
            numbers = text_to_float(numbers)
            return numbers[0] - numbers[1]


def mult(numbers):
    if numbers[0].isdigit() and numbers[1].isdigit():
        return int(numbers[0]) * int(numbers[1])
    else:
        if type(text_to_float(numbers)) == "str":
            return text_to_float(numbers)
        else:
            numbers = text_to_float(numbers)
            return numbers[0] * numbers[1]

def div(numbers):
    if numbers[0].isdigit() and numbers[1].isdigit():
        return int(numbers[0]) / int(numbers[1])
    else:
        if type(text_to_float(numbers)) == "str":
            return text_to_float(numbers)
        else:
            numbers = text_to_float(numbers)
            return numbers[0] / numbers[1]