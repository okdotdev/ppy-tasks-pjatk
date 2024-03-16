import numpy as np


def get_random_number_from_a_to_b(a, b):
    return np.random.uniform(a, b)


def get_random_2d_array(n):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            # Sprawdzam, czy znajduje się ponad jedną z dwóch przekątnych
            if i < j or i + j < n - 1:
                A[i][j] = get_random_number_from_a_to_b(-3 * i - 1, 5 * j + 4)
            else:
                # Liczby większe od 1 lub mniejsze od 7
                A[i][j] = get_random_number_from_a_to_b(2, 6)
    return A


def move_columns(A, condition, K):
    sum_of_columns = np.sum(A, axis=0)
    columns_to_move = np.where(sum_of_columns > condition)[0]
    if len(columns_to_move) > 0:
        for column in columns_to_move:
            A[:, column] = np.roll(A[:, column], -2)
    else:
        for column in range(len(A[0])):
            A[:, column] = np.roll(A[:, column], K)
    return A


def print_array(A):
    for row in A:
        print(row, sep=",")


def main():
    n = int(input("Wpisz n:"))
    A = get_random_2d_array(n)
    print_array(A)
    condition = float(input("Podaj liczbę dla warunku przesunięcia kolumn: "))
    K = 3  # Stała dla przesunięcia w dół
    A = move_columns(A, condition, K)
    print_array(A)


if __name__ == '__main__':
    main()
