'''
Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа nn и mm, количество строк и столбцов, соответственно.
Далее следуют nn строк, содержащих по mm целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести mm строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.
'''

length = list(input().split())
N = int(length[0])
M = int(length[1])
list1 = list()
list2 = list()
list3 = list()
list4 = list()
for i in range(N):
    list1.append(input())
for r in range(N):
    list3.append([])
    list2 = list1[r].split()
    for c in range(M):
        list3[r].append([list2[c]])
'''
for i in range(N):
    for j in range(M):
        list3[i][j] = list3[j][i]
print(list4)
'''


def transp(height, width, matrix):
    return [[matrix[row][col] for row in range(0,height)] for col in range(0,width) ]
list4 = transp(N,M,list3)
for i in list4:
    for j in i:
        for k in j:
            print(k, end = ' ')
    print('')
# print(transp(N,M,list3))
