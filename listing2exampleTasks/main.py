import random

# zadanie 6

class RecordNode:
    def __init__(self, name, surname, age=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.next = None


class RecordLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, name, surname, age=None):
        new_node = RecordNode(name, surname, age)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_author_record(self, author_name, author_surname):
        self.insert_at_end(author_name, author_surname)

    def remove_second_node(self):
        if not self.head or not self.head.next:
            return RecordNode("?", "?", 0)

        second_node = self.head.next
        self.head.next = second_node.next
        return second_node


# zadanie 7
class RealNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class RealLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = RealNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove_node_by_index(self, index):
        if not self.head:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        prev = None
        current = self.head
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current:
            prev.next = current.next
            return True

        return False

    def calculate_average_positive(self):
        count = 0
        total = 0.0
        current = self.head

        # Zliczanie dodatnich elementów i sumowanie ich wartości
        while current:
            if current.data > 0:
                total += current.data
                count += 1
            current = current.next

        # Obliczanie średniej wartości
        if count > 0:
            average = total / count
            return average
        else:
            return None


# zadanie 8
class NameAgeNode:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None


class NameAgeLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, name, age):
        new_node = NameAgeNode(name, age)
        new_node.next = self.head
        self.head = new_node

    def delete_first_occurrence(self, name):
        if not self.head:
            return None

        if self.head.name == name:
            age = self.head.age
            self.head = self.head.next
            return age

        prev = self.head
        current = self.head.next
        while current:
            if current.name == name:
                age = current.age
                prev.next = current.next
                return age
            prev = current
            current = current.next

        return None

    # zadanie 9


class StrNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = StrNode(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def move_element(self, target_index):
        if not self.head or not self.head.next:
            return None

        prev = None
        current = self.head
        count = 0

        while current.next:
            count += 1
            if count == target_index:
                prev = current
            current = current.next

        if not prev:
            return None

        last_node = current
        prev.next = current.next
        last_node.next = prev.next.next
        prev.next.next = last_node

        return prev.next.data if prev.next else None


#  zadanie10
class PairIntNode:
    def __init__(self, liczba1, liczba2):
        self.liczba1 = liczba1
        self.liczba2 = liczba2
        self.next = None


class PairIntLinkedList:
    def __init__(self):
        self.head = None

    def append(self, liczba1, liczba2):
        new_node = PairIntNode(liczba1, liczba2)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_and_append(self):
        if not self.head or not self.head.next:
            return None

        # Usuwanie pierwszego elementu
        first_node = self.head
        self.head = first_node.next
        first_node.next = None

        # Znajdowanie elementu o największej wartości liczba1
        max_liczba1 = float('-inf')
        current = self.head
        while current:
            max_liczba1 = max(max_liczba1, current.liczba1)
            current = current.next

        # Dodawanie nowego elementu z największą wartością liczba1
        new_liczba2 = 42  # Możesz tutaj ustawić jakąś wartość, np. 42
        new_node = PairIntNode(max_liczba1, new_liczba2)
        if not self.head:
            self.head = new_node
            return new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

        return new_node


def main():
    print("Hello world!")


if __name__ == "__main__":
    main()
