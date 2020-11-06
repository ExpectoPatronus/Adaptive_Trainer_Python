'''
Напишите простой интерпретатор математического выражения.

На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором: a \texttt{ operator } ba operator b, где вместо \texttt{operator}operator могут использоваться следующие слова: plus, minus, multiply, divide для, соответственно, сложения, вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a \texttt{ operator } ba operator b, 0 \le a,b\le10000≤a,b≤1000. Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число -− результат вычисления
'''

list1 = input().split()
list2 = ['plus', 'minus', 'multiply', 'divide']
operator = list1[1]
try:
    a = int(list1[0])
    b = int(list1[2])
except:
    print("Error")
    quit()
if len(list1)!= 3:
    print("Error")
    quit()
if (a > 1000 or a<0) or (b > 1000 or b<0):
    print("Error")
    quit()
if operator not in list2:
    print("Error")
    quit()


def outp(n1,n2,oper):
    if oper == 'plus':
        return int(n1+n2)
    if oper == 'minus':
        return int(n1 - n2)
    if oper == 'multiply':
        return int(n1*n2)
    if oper == 'divide':
        return int(n1/n2)
res =outp(a,b,operator)
print(res)