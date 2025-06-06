class Node:
    def __init__(self, value):
        self.data = str(value)
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None  # Points to the last node in the circular list

    def InsertAtBegin(self, data):

        node = Node(data)

        if not self.last:
            # First node, point to itself
            self.last = node
            self.last.next = node
        else:
            # Insert after last, update last.next to new head
            node.next = self.last.next
            self.last.next = node

    def InsertAtLast(self, data):
        node = Node(data)
        if not self.last:
            self.last = node
            self.last.next = node
        else:
            node.next = self.last.next
            self.last.next = node
            self.last = node

    def GetLength(self):

        if not self.last:
            return 0

        count = 1
        current = self.last.next  # Start from head

        while current != self.last:
            count += 1
            current = current.next

        return count

    def InsertAt(self, data, index):
        length = self.GetLength()
        if index < 0 or index > length:
            print("Invalid index")
            return

        if index == 0:
            self.InsertAtBegin(data)
            return
        if index == length:
            self.InsertAtLast(data)
            return

        current = self.last.next
        count = 0

        while count < index - 1:
            current = current.next
            count += 1

        node = Node(data)
        node.next = current.next
        current.next = node

    def print_list(self):
        if self.last is None:
            print("Empty list")
            return

        current = self.last.next
        while True:
            print(current.data, end="-->")
            current = current.next
            if current == self.last.next:
                break
        print()

    def RemoveAtStart(self):
        if not self.last:
            print("Empty linkedlist")
            return
        current = self.last.next
        self.last.next = current.next

    def RemoveAtEnd(self):
        if not self.last:
            print("Empty linkedlist")
            return
        current = self.last.next
        while True:
            if current.next == self.last:
                break
            current = current.next
        current.next = self.last.next
        self.last = current

    def RemoveAt(self, index):
        length = self.GetLength()
        if not self.last or index < 0 or index >= length:
            print("Invalid index")
            return

        if index == 0:
            self.RemoveAtStart()
            return
        if index == length - 1:
            self.RemoveAtEnd()
            return

        current = self.last.next
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
        current.next = current.next.next


if __name__ == "__main__":
    l1 = CircularLinkedList()
    l1.InsertAtBegin(10)
    l1.InsertAtBegin(5)
    l1.InsertAtLast(15)
    print(l1.GetLength())
    l1.print_list()
    l1.InsertAt(7, 1)
    l1.InsertAt(4, 0)
    l1.InsertAt(16, 5)
    l1.InsertAt(12, 4)
    l1.print_list()
    l1.RemoveAtStart()
    l1.RemoveAtEnd()
    l1.print_list()
    l1.RemoveAt(1)
    l1.print_list()
