# Свистунова Марина, 2ИВТ(1.2)
# Задание 4.1 - 4.3
''' 4.1. Создание программы по заполнению массивов случайными значениями. Сортировка значений в списке методом вставки, 
         плавной сортировки, с помощью встроенных функций языка.
    4.2. Создание программы по распределению списка с случайными значениями на два списка по определенному критерию 
         (четность/нечетность, положительные/отрицательные числа).
    4.3. Формирование отчета по практическому заданию и публикация его в портфолио. '''

# метод вставки
def insertionSort(mas = []):
    n = len(mas)
    for i in range(1, n):
        elChange = mas[i]
        k = i - 1
        while ((k >= 0)&(mas[k] > elChange)):
            mas[k + 1] = mas[k]
            k -= 1
        mas[k + 1] = elChange
    return mas

# a = [3, 7, 4, 9, 5, 2, 6, 1, -1, -8, 34, -35, 3425345, -345435243]
# print(insertionSort(a))

# разделение списка на два списка по признаку "положительные/отрицательные числа"
def separateList(mas = []):
    mas1 = []
    mas2 = []
    for i in mas:
        if (i >= 0):
            mas1 += [i]
        else:
            mas2 += [i]
    return mas, mas1, mas2

# print(separateList(a))




#
# def separateDict(d = {}):
#     '''+
#     деление массива по четности значений
#     '''
#     list = d.items()
#
#
# # плавная сортировка
# # def sortNumLeonardo(a, b):
# #     check = {1: 1, 2: 3, 3: 5, 4: 9, 5: 15}
# #     if (b == check.get(a - 1) or b == check.get(a + 1)):
# #         return 1
# #     else:
# #         return -1
# #
# # def smoothSort(mas = []):
# #     n = len(mas)
# #     firstMas = [mas[0]]
# #     secondMas = []
# #     for i in range(1, n):
# #         if sortNumLeonardo(len(firstMas), len(secondMas)) == 1:
# #             firstMas += [secondMas]
# #             firstMas += mas[i]
# #             secondMas = []
# #             maxEl
# #     pass
