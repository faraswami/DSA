from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        return self.queue.appendleft(str(data))

    def dequeue(self):
        return self.queue.pop()

    def show(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

    def IsEmpty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    queue = []
    queue.insert(0, 5)
    queue.insert(0, 10)
    print(queue)
    queue.pop()
    print(queue)

    q1 = Queue()
    q1.enqueue(5)
    q1.enqueue(10)
    q1.enqueue(15)
    q1.show()
    q1.dequeue()
    q1.show()
    print(q1.size())
    print(q1.IsEmpty())

    print("---------------")

    pq = Queue()

    pq.enqueue(
        {"company": "Wall Mart", "timestamp": "15 apr, 11.01 AM", "price": 131.10}
    )
    pq.enqueue({"company": "Wall Mart", "timestamp": "15 apr, 11.02 AM", "price": 132})
    pq.enqueue({"company": "Wall Mart", "timestamp": "15 apr, 11.03 AM", "price": 135})
    pq.show()
    pq.size()
