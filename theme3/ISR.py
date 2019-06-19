# Свистунова Марина, 2ИВТ(1.2)
# Задание 2.1 - 2.4 
''' 2.1. Разработать прототип программы "Калькулятор", позволяющую выполнять базовые арифметические действия и функцию обертку,
         сохраняющую название выполняемой операции, аргументы и результат в файл.  [ без использования '@' ]
    2.2. Дополнение программы "Калькулятор" декоратором, сохраняющим выполняемые действия, в файл-журнал. 
    2.3. Рефакторинг (модификация) программы с декоратором модулем functools и использование его функционала.
    2.4. Формирование отчета по практическому заданию и публикация его в портфолио. '''

# NUMBER 1
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
def decor(f):
    journal = open("journal.txt", "a")
    res = f(str(input()))
    operator, result = res
    journal.write("Операция: ")
    journal.write(operator)
    journal.write(", результат: ")
    journal.write(result)
    journal.write("\n")
decor(culc)


# NUMBER 2
def decor(f):
    def second(*args, **kwargs):
        journal = open("journal.txt", "a")
        operator, result = f(*args)
        journal.write("Операция: ")
        journal.write(operator)
        journal.write(", результат: ")
        journal.write(result)
        journal.write("\n")
        return f(*args, **kwargs)
    return second
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
@decor
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
culc('67*8')


# NUMBER 3
import functools
def decor(f):
    @functools.wraps(f)
    def second(*args, **kwargs):
        journal = open("journal.txt", "a")
        operator, result = f(*args)
        journal.write("Операция: ")
        journal.write(operator)
        journal.write(", результат: ")
        journal.write(result)
        journal.write("\n")
        # return f(*args, **kwargs)
    return second
def is_digit(string):
    if string.isdigit():
       return int(string)
    else:
        try:
            float(string)
            return float(string)
        except ValueError:
            return False
@decor
def culc(strForCulc):
    outp = strForCulc
    str2 = list(strForCulc)
    operators ={
        '+': (lambda x, y: x + y),
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y),
        '^': (lambda x, y: x ** y)
    }
    operators2 = {
        '+': 'addition',
        '-': 'subtraction',
        '*': 'multiplication',
        '/': 'division',
        '^': 'exponentiation'
    }
    operator = ''
    num = ''
    for i in str2:
        if i in '0123456789.' and operator == '':
            num += i
        elif operator == '':
            x = int(num)
            if i in operators:
                operator = i
            num = ''
        else:
            num += i
    y = int(num)
    outp += ' = '
    lr = (operators.get(operator)(x, y))
    outp += str(lr)
    #outp2 = outp + ' = ' + str(lr)
    res2 = operators2.get(operator)
    return [res2, outp]
culc('666*666')
