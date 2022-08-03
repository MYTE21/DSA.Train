from unittest import TestCase
from doubly_linked_list import *


class TestDoublyLinkedList(TestCase):
    def test_append(self):
        dll = DoublyLinkedList()

        assert dll.head.next is None, 'linked list empty, so head should point to None'

        item = 5
        dll.append(item)
        assert dll.head.next.data == item, 'head should point to the first node'

        second_item = 8
        dll.append(second_item)
        assert dll.head.next.data == item, 'head should point to the first node'

        first_node = dll.head.next
        second_node = first_node.next
        assert first_node.next.data == second_item, 'first node should point to second node'

        assert second_node.prev.data == item, 'previous node of second_node should be the first node'
        assert str(dll) == '5,8', 'string representation of dll should match 5,8'

    def test_prepend(self):
        self.fail()

    def test_search(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove(self):
        self.fail()
