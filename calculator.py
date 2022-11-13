def input(message):
    message = message.replace(' ', '')
    if message.find('+') > 0:
        if len(message.split('+')) == 2:
            return summ(message.split('+'))
        else:
            return "Можно сложить только два числа."


    else:
        return "Не могу понять что считать.."



def summ(numbers):
    if numbers[0].isdigit and numbers[0].isdigit:
        return int(numbers[0]) + int(numbers[1])
    # else:
    #     if numbers[0].find('.') > 0:

