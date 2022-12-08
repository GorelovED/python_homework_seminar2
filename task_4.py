# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.



# from random import randint

# def list(n):
#     list = []
#     for i in range(n):
#         list.append(randint(-n, n))
#     return list
# n = int(input('Введите значение N: '))
# numbers = list(n)
# print(numbers)
# p = 1
# path = 'file.txt'
# with open(path, 'r') as data:
#     for line in data:
#         p *= list[int(numbers)] 
#     print(p)

n = int(input("Введите значение N: "))

list_n = []
for i in range(-abs(n), abs(n) + 1):
    list_n.append(i)
print(list_n)

p = 1
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        p *= list_n[int(line)] 
    print(p)
