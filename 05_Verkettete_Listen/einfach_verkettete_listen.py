# Folgende Anforderungen sind gegeben:
# - main mit exemplarischen (Zufallszahlen) Befüllen
# - iterator protokoll implementieren


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.Head = None

    def insert_into_list(self, node):
        newNode = Node(node)
        if self.Head is None:
            self.Head = newNode
        else:
            current = self.Head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def print_whole_list(self):
        current = self.Head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def print_length_of_list(self):
        current = self.Head
        length = 0
        while current is not None:
            current = current.next
            length = length + 1
        return length


if __name__ == '__main__':
    LinkedList = LinkedList()
    LinkedList.insert_into_list(3)
    LinkedList.insert_into_list(10)
    LinkedList.insert_into_list(400)

    print(LinkedList.print_whole_list())
