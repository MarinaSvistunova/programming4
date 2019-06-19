# Свистунова Марина, 2ИВТ(1.2)
# Задание 2.1
''' 2.1. Разработка функции-декоратора, вычисляющей время выполнения декорируемой функции. '''

import time

def time_decore(func):
    print(time.asctime(), end='')
    return func

@time_decore
def tryDecore():
    print(' - дата выполнения этой функции')

tryDecore()
