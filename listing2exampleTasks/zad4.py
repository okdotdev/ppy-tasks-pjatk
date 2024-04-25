import random


def nazwy():
    name = input("Podaj nazwy odzielone spacjami: ")
    lista = name.split(" ")
    return lista


def przsuniecia(arrA):
    for i in range(len(arrA[0])):
        first_name_length = len(arrA[0][i][0])
        last_name_length = len(arrA[-1][i][0])
        if first_name_length > last_name_length:
            tmp = arrA[-1][i]
            for j in range(len(arrA) - 1, 0, -1):
                arrA[j][i] = arrA[j - 1][i]
            arrA[0][i] = tmp


def doublePrint(arrA):
    lista = []
    for i in range(len(arrA)):
        for j in range(len(arrA[i])):
            if j == len(arrA) - 1:
                element = arrA[i][j]
                lista.append(element[0])
    ciagZnakow = ''.join(lista)
    relist = list(ciagZnakow)
    random_elements = random.sample(relist, 2)
    return relist, random_elements


def dwaforB(arr):
    max_value = float('-inf')  # ustawiamy na najmniejszą możliwą wartość
    max_column = None
    # Iteracja po kolumnach
    for i in range(len(arr[0])):
        column_values = [row[i][1] for row in arr]  # zbierz wartości z danej kolumny
        column_max = max(column_values)  # znajdź maksymalną wartość w kolumnie
        if column_max > max_value:
            max_value = column_max
            max_column = i
    # Wydrukowanie kolumny z największą wartością
    print("Kolumna z największą wartością:")
    for row in arr:
        print(row[max_column])
    # Wylosowanie trzech znaków z napisów w kolumnie z największą wartością
    selected_column = [row[max_column][0] for row in arr]  # zbierz napisy z wybranej kolumny
    selected_column = [random.choice(word) for word in selected_column]  # wylosuj jeden znak z każdego napisu
    print("Wylosowane trzy znaki z kolumny:")
    print(selected_column)


def toZeroinDigtal(arr):
    listset = set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j or i + j == len(arr) - 1:
                element = arr[i][j]
                listset.add(element[0])
    posortowane_elementy = sorted(listset, key=len, reverse=True)
    dwie_pierwsze = posortowane_elementy[:2]
    print(dwie_pierwsze)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i == j or i + j == len(arr) - 1) and arr[i][j][0] in dwie_pierwsze:
                arr[i][j][1] = 0


nazwa = nazwy()
rozmiar = 3
arr = [
    [
        [nazwa[random.randint(0, len(nazwa) - 1)], random.randint(-8, 8)]
        for i in range(rozmiar)
    ]
    for j in range(rozmiar)
]
for i in arr:
    print(i)
przsuniecia(arr)
print()
for i in arr:
    print(i)
print(doublePrint(arr))

print(
)
toZeroinDigtal(arr)
print(
)
for i in arr:
    print(i)
