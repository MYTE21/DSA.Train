from binarytree import build


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def parent(i):
    return i // 2


def is_max_heap(heap):
    n = len(heap) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if heap[p] < heap[i]:
            return False

    return True


def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)


def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size // 2, 0, -1):
        max_heapify(heap, heap_size, i)


def print_tree(tree):
    temp_tree = tree[1:]
    root = build(temp_tree)
    print(root)


if __name__ == "__main__":
    # Is the list Max Heap
    print("Is the list Max Heap: ")
    h = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(h, is_max_heap(h))

    h = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
    print(h, is_max_heap(h))

    h = [None, 1, 2, 3]
    print(h, is_max_heap(h))

    h = [None, 2, 1, 3]
    print(h, is_max_heap(h))

    h = [None, 3, 1, 2]
    print(h, is_max_heap(h))

    # Max Heapify method
    print("\nMax Heapify: ")
    h = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
    print(h)
    max_heapify(h, 9, 3)
    print(h)

    h = [None, 1, 2, 3]
    print(h)
    max_heapify(h, 3, 1)
    print(h)

    # Build Max Heap
    print("\nBuild Max Heap:")
    h = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print("Before building heap: ")
    print(h)
    print_tree(h)

    build_max_heap(h)
    print("After building heap: ")
    print(h)
    print_tree(h)