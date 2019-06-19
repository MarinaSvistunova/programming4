# Свистунова Марина, 2ИВТ(1.2)
# Задание 4.3 
''' 4.3. Создание программы, позволяющей выполнять основные операции (объединение, пересечение, вычитание) над множествами 
         (количество множеств и их элементы вводятся вручную). '''

class Arrays:

    def __init__(self, i = 0):
        d = int(input('Введите количество множеств: '))
        f = [[] for i in range(d)]
        print('Введите элементы множеств без запятых через пробел, каждое множество записывается с новой строки')
        for i in range(d):
            k = input().split(' ')
            f[i] += k
        # print(f)
        operation = input('Введите одну из операций: объединение, пересечение или вычитание ')
        if operation == 'объединение':
            print(self.grouping(*f))
        if operation == 'пересечение':
            print(self.crossing(*f))
        if operation == 'вычитание':
            print(self.substraction(*f))

    def grouping(self, *iterable, seen=[]):
        # Функция возвращает список уникальных элементов. В функцию может быть передано различное количество элементов
        if len(seen) == 0:
            seen = list()
        for item in iterable:
            if type(item) == list:
                for item2 in item:
                    if item2 not in seen:
                        seen.append(item2)
            else:
                if item not in seen:
                    seen.append(item)
        return list(seen)

    def crossing(self, *iterable, seen=[]):
        if len(seen) == 0:
            seen = list()
        k = 0
        for item in iterable[0]:
            for i in range(1, len(iterable)):
                if item not in iterable[i]:
                    k = 1
            if k == 0:
                seen.append(item)
            else:
                k = 0
        return list(seen)

    def substraction(self, *iterable, seen=[]):
        if len(seen) == 0:
            seen = iterable[-1]
        seen3 = list()
        for i in range(len(iterable) - 2, -1, -1):
            seen2 = iterable[i]
            for item in seen2:
                if item not in seen:
                    seen3.append(item)
            seen = seen3
            seen3 = list()
        return list(seen)

Arrays()
