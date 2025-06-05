class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = str(data)
        self.prev = prev
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def Printlist(self):
        current = self.head
        strng = ""
        if not current:
            print("Empty linked list")
            return

        while current:
            strng = strng + "<-->" + str(current.data)
            current = current.next
        print(strng)

    def GetLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def InsertAtBegin(self, data):
        if not self.head:
            self.tail = self.head = Node(data)

        else:
            node = Node(data, next=self.head)
            self.head.prev = node
            self.head = node

    def InsertAtEnd(self, data):
        if not self.head:
            self.tail = self.head = Node(data)
        else:
            node = Node(data, prev=self.tail)
            self.tail.next = node
            self.tail = node

    def InsertAt(self, data, index):
        if index < 0:
            print("Not a valid index")
            return

        if index == 0:
            self.InsertAtBegin(data)
            return

        # Traverse to index - 1
        current = self.head
        count = 0

        while current:
            if count == index - 1:
                if current.next is None:
                    # Append at the end
                    self.InsertAtEnd(data)
                else:
                    new_node = Node(data, prev=current, next=current.next)
                    current.next.prev = new_node
                    current.next = new_node
                return
            current = current.next
            count += 1

        # If index is beyond length
        print("Not a valid index")

    def InsertValues(self, data):
        for item in data:
            self.InsertAtEnd(item)

    def RemoveAtEnd(self):
        if not self.tail:
            print("Empty LinkedList")
            return

        if self.head == self.tail:
            # Only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def RemoveAtStart(self):
        if not self.head:
            print("Empty LinkedList")
            return

        if self.head == self.tail:
            # Only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def RemoveAt(self, index):
        if not self.head:
            print("Empty LinkedList")
            return

        if index < 0:
            print("Not a valid index")
            return

        # Remove head
        if index == 0:
            self.RemoveAtStart()
            return

        current = self.head
        count = 0

        while current:
            if count == index:
                if current == self.tail:
                    self.RemoveAtEnd()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            count += 1
            current = current.next

        print("Not a valid index")  # Index beyond list length


if __name__ == "__main__":
    l1 = Linkedlist()
    l1.InsertAtBegin(15)
    l1.InsertAtBegin(10)
    l1.Printlist()
    l1.InsertAtEnd(20)
    l1.Printlist()
    l1.InsertAt(17, 2)
    l1.Printlist()

    l2 = Linkedlist()
    l2.InsertValues(["white", "black", "orange"])
    l2.Printlist()
    l2.InsertAt("green", 2)
    l2.Printlist()
    l2.RemoveAt(3)
    l2.Printlist()
