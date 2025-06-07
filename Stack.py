from collections import deque


class stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(str(data))

    def pop(self):
        return self.stack.pop()

    def peep(self):
        return "Empty List" if self.IsEmpty() else self.stack[-1]

    def size(self):
        return len(self.stack)

    def IsEmpty(self):
        return len(self.stack) == 0

    def show(self):
        print(self.stack)


if __name__ == "__main__":
    s = []
    s.append("banana")
    s.append("apple")
    s.append("mango")
    print(s)
    print(s[-1])
    s.pop()
    print(s)

    # List in python is using dynamic array. If list size is 10 and we want to Insert 11th element then it has to
    # copy entire list to new location. If we define list size as 10 it usually creates 10*2 size of list.

    # Collection.deque is implemented using doubly linked list.
    # Link: https://docs.python.org/3/library/collections.html#collections.deque

    s1 = stack()
    s1.push(5)
    s1.push(10)
    s1.show()
    print(s1.peep())
    print(s1.IsEmpty())
    print(s1.size())
    s1.pop()
    s1.show()
