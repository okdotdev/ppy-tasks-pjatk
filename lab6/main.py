import random

carr_brands = ["Toyota", "Ford", "Volkswagen", "BMW", "Audi", "Mercedes", "Honda", "Chevrolet", "Nissan", "Fiat"]


class Car:
    def __init__(self, brand, year_of_production, price):
        self.brand = brand
        self.year_of_production = year_of_production
        self.price = price


def fill_car_list(size):
    car_array = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            brand = random.choice(carr_brands)
            year_of_production = random.randint(1990, 2024)
            price = round(random.uniform(5000, 50000), 2)
            car_array[i][j] = Car(brand, year_of_production, price)

    return car_array


def increase_price(car_array):
    for j in range(len(car_array[0])):

        if any(car_array[i][j] for i in range(len(car_array))):
            price_of_youngest_car = min(
                car.year_of_production for row in car_array for car in row if
                car != row[-1] and car != car_array[-1][j] and car != car_array[0][j])

            while car_array[-1][j].price > car_array[0][j].price:
                for i in range(len(car_array) - 1):
                    car_array[i][j].price += price_of_youngest_car

                if car_array[-1][j].price >= car_array[0][j].price:
                    break


def print_data(car_array):
    oldest_car_year_of_production = None
    for i in range(len(car_array)):
        for j in range(len(car_array[i])):
            if i < j:
                if oldest_car_year_of_production is None or car_array[i][j].year_of_production < oldest_car_year_of_production:
                    oldest_car_year_of_production = car_array[i][j].year_of_production

    if oldest_car_year_of_production is None:
        print("Brak aut w tablicy spełniających warunki.")
        return

    for row in car_array:
        for car in row:
            if 'f' not in car.brand.lower() and 'z' not in car.brand.lower() and car.price < oldest_car_year_of_production:
                print("Marka:", car.brand)
                print("Rok produkcji:", car.year_of_production)
                print("Cena:", car.price)
                print()


def increase_price_on_diagonal_by_percentage(car_list, percentage=15):
    n = min(len(car_list), len(car_list[0]))
    for i in range(n):
        car_list[i][i].price *= 1 + percentage / 100


def main():
    n = int(input("Podaj rozmiar tablicy: "))

    print("Wypełnij pierwszą tablicę:")
    car_array1 = fill_car_list(n)
    increase_price(car_array1)
    print_data(car_array1)

    print("Wypełnij drugą tablicę:")
    car_array2 = fill_car_list(n)
    increase_price(car_array2)
    print_data(car_array2)

    increase_price_on_diagonal_by_percentage(car_array1)
    increase_price_on_diagonal_by_percentage(car_array2)


if __name__ == "__main__":
    main()
