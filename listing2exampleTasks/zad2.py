# zadanie 2

import random


def nazwy():
    name = input("Podaj nazwy odzielone spacjami: ")
    lista = name.split(" ")
    return lista


def changeObw(arr):
    x = input("podaj jedna litere")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr) - 1:
                element = arr[i][j]
                tmp = element[0]
                digits = list(tmp)
                if x in digits:
                    return
                else:
                    print(tmp)


def randomLetter():
    litera1 = random.choice([chr(i) for i in range(ord('a'), ord('h') + 1)])
    litera2 = random.choice([chr(i) for i in range(ord('a'), ord('h') + 1)])
    list = [litera1, litera2]
    return list


def avgNumb(arr):
    sum, counter = 0, 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j < i < len(arr) - j - 1:
                element = arr[i][j]
                wyraz = element[0]
                liczba = element[1]
                lista = list(wyraz)
                if randomLetter() not in lista:
                    print(element)
                    sum += liczba
                    counter += 1
    return sum / counter


def findLongestNames(arr):
    all_names = set()
    for row in arr:
        for element in row:
            all_names.add(element[0])
    sorted_names = sorted(all_names, key=len)
    return sorted_names[:2]


def goToZero(arr):
    longest_names = findLongestNames(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            element = arr[i][j]
            if element[0] in longest_names:
                element[1] = 0


rozmiar = int(input("Podaj rozmiar: "))
nazwa = nazwy()
arr1 = [
    [
        [nazwa[random.randint(0, len(nazwa) - 1)], random.randint(-5 * i - j, 9 * i + j)]
        for i in range(rozmiar)
    ]
    for j in range(rozmiar)
]
for i in arr1:
    print(i)
x = avgNumb(arr1)
print(randomLetter())
print(x)
goToZero(arr1)
for i in arr1:
    print(i)

# arr2 = [
#     [
#         [nazwa[random.randint(0, len(nazwa) - 1)], random.randint(--3*i-2*j, 7*i+j)]
#         for i in range(rozmiar)
#     ]
#     for j in range(rozmiar)
# ]
# changeObw(arr1)
