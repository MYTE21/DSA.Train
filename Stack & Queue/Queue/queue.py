class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return True if self.items == [] else False


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Tahsin")
    q.enqueue("Rafi")
    q.enqueue("Tamim")

    while not q.is_empty():
        person = q.dequeue()
        print(person)