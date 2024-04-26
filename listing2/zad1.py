class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_every_other_element(self):
        if not self.head:
            return

        current = self.head
        while current and current.next:
            if len(current.data) > len(current.next.data):
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
            else:
                current = current.next.next if current.next.next else None

    def insert_new_data(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" , ")
            current = current.next


def main():
    linked_list = LinkedList()

    while True:
        data = input("Podaj dane do wstawienia do listy (lub wpisz 'q' aby zakończyć): ")
        if data == 'q':
            break
        linked_list.append(data)

    print("Lista przed operacją:")
    linked_list.print_list()

    linked_list.delete_every_other_element()

    new_data = input("Podaj nowy element do wstawienia:")
    linked_list.insert_new_data(new_data)

    print("Lista po operacji:")
    linked_list.print_list()


if __name__ == "__main__":
    main()
