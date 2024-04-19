def print_linked_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


def delete_nodes(head):
    count = 0
    while head is not None and head.next is not None:
        if head.next.data[0].islower():
            head.next = head.next.next
            count += 1
        head = head.next
    return count


def move_element_to_the_beginning_of_linked_list(head):
    if head is None or head.next is None or head.next.next is None:
        return head

    prev = head
    current = head.next
    next_node = head.next.next

    while next_node is not None:
        if len(current.data) > len(prev.data) and len(current.data) > len(next_node.data):
            prev.next = next_node
            current.next = head
            head = current
            prev = head
        else:
            prev = current
        current = next_node
        next_node = next_node.next

    return head


class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.next = None


def main():
    user_input = input("Enter a list of strings (split by whitespace): ").split()

    head = Node(user_input[0])
    current_node = head

    for i in range(1, len(user_input)):
        new_node = Node(user_input[i])
        current_node.next = new_node
        current_node = new_node

    print("Initial linked list:")
    print_linked_list(head)
    print()
    print("Number of deleted nodes:", delete_nodes(head))
    print("Linked list after deletion:")
    print_linked_list(head)


if __name__ == "__main__":
    main()
