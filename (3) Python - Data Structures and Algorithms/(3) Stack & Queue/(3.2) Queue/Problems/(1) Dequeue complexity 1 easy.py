class Queue:
    def __init__(self):
        self.items = []
        self.head = 0
        self.tail = -1

    def enqueue(self, item):
        self.items.append(item)
        self.tail += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.head += 1
            return self.items[self.head - 1]

    def is_empty(self):
        return self.head > self.tail
