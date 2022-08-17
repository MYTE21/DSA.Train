class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next

        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ','.join(nodes)

    def append(self, data):
        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return

        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next

        current_node.next = node

    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node

    def insert(self, data, new_data):
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
                break

            current_node = current_node.next

    def search(self, item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node

            current_node = current_node.next

        return None

    def remove(self, item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    print(f"After adding 5 and 10 in the linked list (append): [ {ll} ]")    # 5, 10
    ll.prepend(1)
    print("After adding 1 in the beginning of the linked list (prepend): [ {} ]".format(ll))    # 1, 5, 10
    print("Search of 5 (search): ", ll.search(5), " [means 5 is present in the linked list]")    # 5
    print("Search of 50 (search): ", ll.search(50), " [means the linked list has no element as 50]")    # None
    ll.append(50)
    print("After adding 50 in the linked list (append): [", ll, "]")    # 1, 5, 10, 50
    print("Search of 50 (search): ", ll.search(50), " [now 50 is present in the linked list]")    # 50
    ll.remove(50)
    print(f"After removing 50 from the linked list (remove): [ {ll} ]")    # 1, 5, 10
    ll.insert(5, 6)
    print(f"Inserting 6 after 5 in the linked list (insert): [ {ll} ]")    # 1, 5, 6, 10
    ll.remove(1)
    print(f"After removing 1 from the linked list (remove): [ {ll} ]")    # 5, 6, 10