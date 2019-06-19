# VSR
import time

def time_decore(func):
    print(time.asctime(), end='')
    return func

@time_decore
def tryDecore():
    print(' - дата выполнения этой функции')

tryDecore()
