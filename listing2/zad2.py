import random

deleted_counter = 0


class Node:
    def __init__(self, nazwa, sides_count, field):
        self.name = nazwa
        self.sides_count = sides_count
        self.field = field
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_element(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def print(self):
        current = self.head
        while current:
            print("Nazwa:", current.name)
            print("Liczba boków:", current.sides_count)
            print("Pole powierzchni:", current.field)
            print("--------------------")
            current = current.next

    def get_m_element_from_the_end_of_the_list(self, M):

        if self.head is None:
            return None

        if self.head.next is None:
            return None

        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if count < M:
            return None
        current = self.head
        for i in range(count - M):
            current = current.next
        return current

    def delete_elements(self):
        global deleted_counter

        prev = None
        current = self.head
        while current:
            if deleted_counter == 3:
                break

            M = random.randint(1, 10)
            m_element_from_the_end = self.get_m_element_from_the_end_of_the_list(M)

            if m_element_from_the_end is None:
                return

            if current.sides_count % 2 == 0 and current.field < m_element_from_the_end.field:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                deleted_counter += 1
            else:
                prev = current
            current = current.next

    def append_element_after_first_element_containing_only_characters_provided(self, node, characters: str):
        current = self.head
        while current:
            if all(char in current.name for char in characters):
                node.next = current.next
                current.next = node
                break
            current = current.next

        element_tuple: tuple = (current.name, current.sides_count, current.field)
        return element_tuple


def main():
    linked_list = LinkedList()

    while True:
        name = input("Podaj nazwę figury: ")
        if name == "":
            break
        sides = int(input("Podaj liczbę boków: "))
        field = float(input("Podaj pole powierzchni: "))
        linked_list.append_element(Node(name, sides, field))

    print("Lista:")
    linked_list.print()
    linked_list.delete_elements()

    print("Usunięto elementów:", deleted_counter)

    print("Lista po usunięciu elementów:")
    linked_list.print()

    text: str = input("Podaj nazwę nowej  figury: ")
    sides: int = int(input("Podaj liczbę boków nowej figury: "))
    field: float = float(input("Podaj pole powierzchni nowej figury: "))

    characters = input("Podaj ciąg znaków: ")

    linked_list.append_element_after_first_element_containing_only_characters_provided(Node(text, sides, field),
                                                                                       characters)

    print("Lista po dodaniu nowego elementu:")
    linked_list.print()


if __name__ == "__main__":
    main()
