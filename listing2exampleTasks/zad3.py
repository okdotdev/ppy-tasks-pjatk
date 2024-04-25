# zadanie 3
import random

class Samochod:
    def __init__(self, marka, rok_produkcji, cena):
        self.marka = marka
        self.rok_produkcji = rok_produkcji
        self.cena = cena
    def __repr__(self):
        return f"(marka={self.marka}, rok_produkcji={self.rok_produkcji}, cena={self.cena})"

marki_samochodow = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen", "BMW", "Mercedes-Benz", "Audi", "Nissan",
                    "Hyundai"]
#automatyczny kronstruktor
def createCar():
    marka = random.choice(marki_samochodow)
    rok_produkcji = random.randint(2000, 2024)
    cena = random.randint(0, 100000)
    return Samochod(marka, rok_produkcji, cena)
# zwiększać cenę ostatniego auta w danym wierszu o cenę najstarszego auta
# znajdującego się na lewo od obydwu przekątnych, w danym wierszu dopóki cena
# pierwszego auta w danym wierszu jest większa od ceny ostatniego auta w danym
# wierszu
def changeCena(arr):
    for i in range(len(arr)):
        first_car_price = arr[i][0].cena  # Cena pierwszego samochodu w danym wierszu
        last_car_price = arr[i][-1].cena  # Cena ostatniego samochodu w danym wierszu
        # Jeśli cena pierwszego samochodu jest większa od ceny ostatniego samochodu w danym wierszu
        if first_car_price > last_car_price:
            for j in range(len(arr[i])):
                arr[i][
                    -1].cena += last_car_price  # Zwiększ cenę ostatniego samochodu w danym wierszu o cenę ostatniego samochodu
    cars = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j < i < len(arr) - j - 1:
                cars.append(arr[i][j])
    najtansze_auto = None
    minCena = float('inf')
    for samochod in cars:
        if samochod.cena < minCena:
            minCena = samochod.cena
            najtansze_auto = samochod
    if najtansze_auto:
        print("Najtańsze auto:")
        print(najtansze_auto)
    else:
        print("Brak samochodów")
# wydrukować dane aut, których marka nie zawiera żadnej litery ‘d’ i ‘k’ oraz cena
# jest mniejsza od ceny najstarszego auta znajdującego się na lewo od obydwu
# przekątnych
def printCArs(arr):
    cars = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j < i < len(arr) - j - 1:
                cars.append(arr[i][j])
    najstarsze_auto = None
    minRok = float('inf')
    for samochod in cars:
        if samochod.rok_produkcji < minRok:
            minRok = samochod.rok_produkcji
            najstarsze_auto = samochod
    if najstarsze_auto:
        print("Najtańsze auto:")
        print(najstarsze_auto)
    else:
        print("Brak samochodów")
    print()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if ("k" in arr[i][j].marka or "d" in arr[i][j].marka) and najstarsze_auto.cena > arr[i][j].cena:
                print(arr[i][j])
#zwiększanie cen dwóch natańszych samochodów znajdujących sie na przekątnych
def toZero(arr):
    ceny = set()
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                ceny.add(arr[i][j].cena)
    najtansze_ceny = sorted(ceny)[:2]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                if arr[i][j].cena in najtansze_ceny:
                    arr[i][j].cena = arr[i][j].cena*1.15
    return arr

x = 3
arr1 = [[createCar() for i in range(x)] for j in range(x)]
for i in arr1:
    print(i)
toZero(arr1)
print()
for i in arr1:
    print(i)
# printCArs(arr)
# for i in arr:
#     print(i)
# print()
#
# changeCena(arr)
#
# print()
#
# for i in arr:
#     print(i)