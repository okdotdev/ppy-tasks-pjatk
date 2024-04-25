class Figura:
    def __init__(self, nazwa, liczba_bokow, pole_powierzchni):
        self.nazwa = nazwa
        self.liczba_bokow = liczba_bokow
        self.pole_powierzchni = pole_powierzchni
        self.nastepna = None


class ListaJednokierunkowa:
    def __init__(self):
        self.head = None

    def dodaj_element(self, figura):
        if not self.head:
            self.head = figura
        else:
            current = self.head
            while current.nastepna:
                current = current.nastepna
            current.nastepna = figura

    def wyswietl(self):
        current = self.head
        while current:
            print("Nazwa:", current.nazwa)
            print("Liczba boków:", current.liczba_bokow)
            print("Pole powierzchni:", current.pole_powierzchni)
            print("--------------------")
            current = current.nastepna

    def usun_elementy(self):
        current = self.head
        previous = None
        usuniete = 0
        while current and current.nastepna:
            if current.pole_powierzchni > current.nastepna.pole_powierzchni:
                if previous:
                    previous.nastepna = current.nastepna
                else:
                    self.head = current.nastepna
                usuniete += 1
                usuniete += 1
            previous = current
            current = current.nastepna
        return usuniete

    def wstaw_przed_pierwszym_napisem(self, nazwa, liczba_bokow, pole_powierzchni):
        nowy_element = Figura(nazwa, liczba_bokow, pole_powierzchni)
        if not self.head or isinstance(self.head.nazwa, (int, float)):
            nowy_element.nastepna = self.head
            self.head = nowy_element
            return id(nowy_element)
        else:
            current = self.head
            while current.nastepna and not isinstance(current.nastepna.nazwa, (int, float)):
                current = current.nastepna
            nowy_element.nastepna = current.nastepna
            current.nastepna = nowy_element
            return id(nowy_element)


# Tworzenie listy jednokierunkowej
lista_figur = ListaJednokierunkowa()
# Dodawanie przykładowych danych testowych
lista_figur.dodaj_element(Figura("Kwadrat", 4, 16))
lista_figur.dodaj_element(Figura("Trójkąt", 3, 6.5))
lista_figur.dodaj_element(Figura("Koło", "∞", 3))
lista_figur.dodaj_element(Figura("Prostokąt", 4, 20))
lista_figur.dodaj_element(Figura("Trójkąt równoramienny", 3, 10))
# Wyświetlanie listy przed wstawieniem nowego elementu
print("Lista przed wstawieniem nowego elementu:")
lista_figur.wyswietl()
# Usuwanie co drugiego elementu z listy i wyświetlanie liczby usuniętych elementów
liczba_usunietych = lista_figur.usun_elementy()
print("Liczba usuniętych elementów:", liczba_usunietych)
print("Lista po usunięciu elementów:")
lista_figur.wyswietl()
# Wstawianie nowego elementu przed pierwszym napisem zawierającym wyłącznie jakieś znaki
adres_nowego_elementu = lista_figur.wstaw_przed_pierwszym_napisem("Nowy", 0, 0)
# Wyświetlanie listy po wstawieniu nowego elementu
print("Lista po wstawieniu nowego elementu:")
lista_figur.wyswietl()
print("Adres nowego elementu:", adres_nowego_elementu)
