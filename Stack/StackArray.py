# Stack using Array
class StackArr:

    def __init__(self, cap) -> None:
        self.cap: int = cap
        self.a = [0] * cap
        self.top: int = -1

    def push(self, val) -> bool:
        if self.top >= self.cap - 1:
            print("Stack overflow")
            return False
        self.top += 1
        self.a[self.top] = val
        return True

    def pop(self) -> int:
        if self.top < 0:
            print("Stack underflow")
            return -1
        popped = self.a[self.top]
        self.top -= 1
        return popped

    def peek(self):
        if self.top < 0:
            print("Stack is empty")
            return -1
        return self.a[self.top]

    def is_empty(self):
        return self.top < 0


s = StackArr(10)
s.push(10)
s.push(20)
s.push(30)
print(s.pop(), "popped from stack")

print("Top element is:", s.peek())

print("Elements present in stack:", end=" ")
while not s.is_empty():
    print(s.peek(), end=" ")
    s.pop()
