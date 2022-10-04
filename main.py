print_welcome = '''Начало работы программы калькулятор.
            СПРАВКА:
Используемые операторы: +, -, /, *, **
CTRL+С - для выхода из программы'''
print_current_value = 'Введите корректное значение!'
print_result = 'Результат: '
print_cntn = 'Продолжить операцию с результатом? (д/н) '
print_close = 'Завершить работу? (д/н) '
print_exit = 'Завершение работы калькулятора.'
print_input = 'Введите число: '
print_operators = 'Введите знак действия (+, -, /, *, **): '
print_error = 'Ошибка! Введите корректное значение!'
operators = ['+', '-', '/', '*', '**']



def main ():
    print(print_welcome)
    prev_result = 0

    while True:
        try:
            num1, operator, num2 = get_expression(prev_result)
        except ValueError:
            print(print_current_value)
            continue
        except TypeError:
            continue
        except KeyboardInterrupt:
            break

        result = choose_action(num1, operator, num2)

        print(print_result, result)
        try:
            cntn = input(print_cntn)

            if cntn == 'д':
                prev_result = result
            else:
                prev_result = 0
                close = input(print_close)
                if close == 'д':
                    print(print_exit)
                    break
        except KeyboardInterrupt:
            break

def choose_action(num1, operator, num2):

    if operator == '+':
        return addition(num1, num2)
    if operator == '-':
        return subtraction(num1, num2)
    if operator == '/':
        return division(num1, num2)
    if operator == '*':
        return multiplication(num1, num2)
    if operator == '**':
        return exponentiation(num1, num2)

def get_expression(prev_result):
    try:
        if prev_result == 0:
            num1 = float(input(print_input))
        else:
            num1 = prev_result
        operator = input(print_operators)
        if operator not in operators:
            raise ValueError
        num2 = float(input(print_input))
        if operator == '/' and num2 == 0:
            raise ValueError
        return num1, operator, num2
    except ValueError:
        print(print_error)

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1, num2):
    return num1 / num2

def multiplication(num1, num2):
    return num1 * num2

def exponentiation(num1, num2):
    return num1 ** num2

if __name__ == '__main__':
    main()