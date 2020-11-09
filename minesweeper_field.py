'''
Поле для игры сапёр представляет собой сетку размером n \times mn×m. В ячейке сетки может находиться или отсутствовать мина.

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки, не являющейся миной, указывается число мин, находящихся в соседних ячейках (учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1 \le n,m \le 1001≤n,m≤100, после чего в nn строках содержится описание поля в виде последовательности точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
nn строк поля, в каждой ячейке которого будет либо число от 0 до 8, либо мина (обозначенная символом "*"), при этом число означает количество мин в соседних ячейках поля.


'''
import numpy as np

size = input().split()
n = int(size[0])
m = int(size[1])
# n, m = [int(x) for x in input().split()]
test_a = np.zeros((n+2,m+2),dtype=int)
for i in range(n):
    b = list(input())
    for j in range(m):
        if b[j] != '.':
            test_a[i+1,j+1] = -1
# for i in range(n):
#     for j in range(m):
#         if (i, j) in stars:
#             print('*', end='')
#         else:
#             print (sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if (x, y) in stars), end='')
#     print()


for i in range(n):
    for j in range(m):
        if test_a[i+1,j+1] != -1:
            if test_a[i+1,j+2] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i+1,j] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i+2,j+1] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i,j+1] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i+2,j+2] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i,j] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i+2,j] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
            if test_a[i,j+2] == -1:
                test_a[i+1,j+1]=test_a[i+1,j+1]+1
for i in range(n):
    for j in range(m):
        if test_a[i+1,j+1]==-1:
            print('*', end="")
        else:
            print(test_a[i+1,j+1],end="")
    print()