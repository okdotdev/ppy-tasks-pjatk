import math
import random


# zad1
def random_numbers():
    print("Generating 5 random numbers")
    for i in range(5):
        rand: int = random.randint(1, 100)
        print(rand)


# zad2
def get_numbers():
    temp_list: list = []

    for i in range(3):
        temp_list.append(float(input("Input number:")))
    temp_list.sort()

    smallest = temp_list[0]
    biggest = temp_list[len(temp_list) - 1]

    print("Smallest number=" + str(smallest))
    print("Biggest number=" + str(biggest))

    return None


# zad3
def get_pitagoreyans():
    a = float(input("Podaj A:"))
    b = float(input("Podaj B:"))
    c = float(input("Podaj C:"))

    a_square = a ** 2
    b_square = b ** 2
    c_square = c ** 2
    if a_square + b_square == c_square:
        print("Są trójkami pitagorejskimi")
    else:
        print("Nie są trójkami pitagorejskimi")


# zad6
def curious():
    first_two: int
    last_two: int
    for i in range(1000, 9999):
        first_two = i % 100
        last_two = i // 100

        if i == first_two ** 2 + last_two ** 2:
            print("Spełnia zależnosć=" + str(i))


def get_catalans():
    even: int = 0
    odd: int = 0

    for i in range(0, 1000_000):
        num = catalan(i)
        print("Num=" + str(num))
        if num %2 == 0:
            even += 1
        else:
            odd += 1

    print("Even=" + str(even) + " Odd" + str(odd))

    return None


def catalan(n):
    if n == 0:
        return 1
    else:
        return ((4 * n + 2) / (n + 2)) * catalan(n - 1)


def home_work():
    k: int = int(input("Wprowadź k="))

    for index in range(k):
        print("-----------------------------------")
        y: float = float(input("Wprowadź y="))

        result: float = 0
        for x in range(1, 10):
            x /= 10
            if math.sin(x) > math.cos(y):
                for i in range(1, 10, 1):
                    result += (x + y) ** i / math.factorial(i)
            else:
                result = (x ** 5) + (x ** 3 * y ** 2) + (y ** 4)

            print("Dla x=" + str(x) + " Oraz y=" + str(y) + " Wynik=" + str(result))
        print("-----------------------------------")


def main():
    # random_numbers()
    # get_numbers()
    # get_pitagoreyans()
    # curious()
    get_catalans()
    # home_work()


if __name__ == "__main__":
    main()
