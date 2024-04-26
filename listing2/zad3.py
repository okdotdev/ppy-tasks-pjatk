import random
import sys


class Record:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def create_2d_record_array(N, is_tab_a=False):
    print("Tworze Tablice A" if is_tab_a else "Tworze Tablice B")

    record_array = []
    for i in range(N):
        record_array.append([])
        for j in range(N):
            input_name = input("Podaj nazwę: ")
            if is_tab_a:
                record_array[i].append(Record(input_name, random.randint(-9, 6)))
            else:
                record_array[i].append(Record(input_name, random.randint(-7 * i + j, 2 * i + 8 * j)))

    return record_array


def print_2d_record_array(record_array):
    for row in record_array:
        for element in row:
            print(element.name, element.number, end=" ")
        print()


def print_certain_elements(record_array, is_tab_A):
    if is_tab_A:
        for i in range(3):
            row = random.randint(0, len(record_array) - 1)
            element = random.randint(0, len(record_array[row]) - 1)
            print("3 losowe znaki z napisu w wierszu", row, ":", record_array[row][element].name[:3])
    else:
        min_count = sys.maxsize
        min_count_column = 0
        for i in range(len(record_array)):
            count = 0
            for j in range(i):
                count += 1
            if count < min_count:
                min_count = count
                min_count_column = i

        for i in range(len(record_array)):
            print("2 znaki z napisu w kolumnie", min_count_column, ":", record_array[i][min_count_column].name[:2])


def move_cyclically(tab, k):
    for i in range(len(tab)):
        name_of_first = tab[i][0][0]
        for _ in range(k):
            tab[i].append(tab[i].pop(0))
            if len(tab[i][0][0]) < len(name_of_first):
                name_of_first = tab[i][0][0]


def main():
    N = int(input("Podaj rozmiar tablicy: "))
    A = create_2d_record_array(N, True)
    B = create_2d_record_array(N)

    move_cyclically(A, 2)
    move_cyclically(B, 3)

    print("Tablica A:")
    print_certain_elements(A, True)
    print("Tablica B:")
    print_certain_elements(B, False)


if __name__ == "__main__":
    main()
