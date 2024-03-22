import random as r


# 1
def random_numbers():
    return [r.randint(1, 100) for i in range(1000)]


def sort_random_numbers(old_list: list):
    new_list: list = []
    for i in range(len(old_list)):
        if old_list[i] % 7 == 0 and old_list[i] % 5 != 0:
            new_list.append(old_list[i])

    return new_list


# 2
def convert_to_bin(n: int):
    binary: str = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    return binary


# 3
def check_for_lil_sequence_in_big_sequence(sequence: str):
    # TODO implement this function
    return None


# 4
def find_index_of_lil_sequence_in_big_sequence(sequence: str):
    # TODO implement this function
    return None


def main():
    # 1
    a = random_numbers()
    b = sort_random_numbers(a)
    print(b)

    # 2
    print(convert_to_bin(10))


if __name__ == '__main__':
    main()
