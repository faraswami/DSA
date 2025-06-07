## Head --> n1 --> n2 --> (null)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current = self.head
        if not current:
            print("Empty linkedlist")
            return

        strng = ""
        while current:
            strng = strng + "-->" + str(current.data)
            current = current.next
        print(strng)

    def InsertAtStart(self, data):
        node = Node(data, self.head)
        self.head = node

    def InsertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = Node(data, None)
        current = self.head

        while (
            current.next
        ):  # --last current.next would be null so iterate till current-1
            current = current.next  # node with next as null

        current.next = node

    def getlength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def InsertValuesat(self, data, index):
        if index < 0 or index > self.getlength():
            print("Invalid Index")
            return
        if index == 0:
            self.InsertAtStart(data)

        # count = 0
        # node = Node(data)
        # current = self.head
        # while count < index - 1:
        #     count = count + 1
        #     current = current.next
        # if count == index - 1:
        #     temp = current.next
        #     current.next = node
        #     node.next = temp

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
                break

            current = current.next
            count += 1

    def InsertValues(self, data):
        self.head = None
        for item in data:
            self.InsertAtEnd(item)

    def RemoveAt(self, index):
        if index < 0 or index >= self.getlength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            count += 1
            current = current.next

    def reverse_list(head):
        curr = head
        prev = None

        while curr:
            temp_node = curr.next
            curr.next = prev
            prev = curr
            curr = temp_node

        return prev

    def insert_after_value(self, value, data):
        current = self.head
        count = 0
        while current:
            if str(current.data) == str(value):
                self.InsertValuesat(data, count + 1)
                break
            count += 1
            current = current.next

    def remove_by_value(self, value):
        current = self.head

        if str(self.head.data) == str(value):
            self.head = current.next
            return
        while current:
            if str(current.next.data) == str(value):
                current.next = current.next.next
                break
            current = current.next


if __name__ == "__main__":
    l1 = Linkedlist()
    l1.InsertAtStart(2)
    l1.InsertAtStart(1)
    l1.InsertAtEnd(9)
    l1.InsertAtEnd(10)
    l1.printlist()
    print("length:", l1.getlength())
    l1.InsertValuesat(3, 2)
    l1.printlist()

    l2 = Linkedlist()
    l2.InsertValues([5, 10, 15, 20])
    l2.printlist()
    l2.RemoveAt(2)
    l2.printlist()
    l2.insert_after_value(20, 21)
    l2.printlist()
    l2.remove_by_value(5)
    l2.printlist()
