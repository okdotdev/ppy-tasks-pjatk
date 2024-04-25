import random


# zadanie 1
def createArr(nazwa, rozmiar):
    arg = [
        [[nazwa[random.randint(0, len(nazwa) - 1)], random.randint(-8 * i + j, 6 * i + 3 * j)] for i in range(rozmiar)]
        for j in range(rozmiar)]
    return arg


def nazwy():
    name = input("Podaj nazwy odzielone spacjami: ")
    lista = name.split(" ")
    return lista


def diagonalChange(arr):
    rozmiar = len(arr)
    pierwszy_napis_dluzy = True
    ilosc_zmian = 0
    while pierwszy_napis_dluzy:
        index1 = random.randint(0, rozmiar - 1)
        index2 = random.randint(0, rozmiar - 1)
        element1 = arr[index1][index1]
        element2 = arr[index2][rozmiar - 1 - index2]
        pierwsza_dlugosc = len(element1[0])
        druga_dlugosc = len(element2[0])
        if pierwsza_dlugosc > druga_dlugosc:
            arr[index1][index1] = element2
            arr[index2][rozmiar - 1 - index2] = element1
            ilosc_zmian += 1
        else:
            pierwszy_napis_dluzy = False
    print(ilosc_zmian)
    return arr


def pickRandom(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i < j and i > len(arr) - j - 1:
                element = arr[i][j]
                wyraz = element[0]
                print(wyraz)
                wyrazlista = list(wyraz)
                counter = 0
                while counter <= 2:
                    print(wyrazlista[random.randint(0, len(wyrazlista) - 1)], " ", end='')
                    counter += 1


def findLongestNames(arr):
    all_names = set()
    for row in arr:
        for element in row:
            all_names.add(element[0])
    sorted_names = sorted(all_names, key=len, reverse=True)
    return sorted_names[:2]


def goToZero(arr):
    longest_names = findLongestNames(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            element = arr[i][j]
            if element[0] in longest_names:
                element[1] = 0


name = nazwy()
arr = createArr(name, 3)
print("Tablica przed zmianą:")
for i in arr:
    print(i)
print()
diagonalChange(arr)
print("Tablica po zmianie:")
for i in arr:
    print(i)
pickRandom(arr)
goToZero(arr)
for i in arr:
    print(i)
