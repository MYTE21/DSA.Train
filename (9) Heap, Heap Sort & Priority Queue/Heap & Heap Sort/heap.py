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


if __name__ == "__main__":
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
    print(H, is_max_heap(H))

    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
    print(H, is_max_heap(H))

    H = [None, 1, 2, 3]
    print(H, is_max_heap(H))

    H = [None, 2, 1, 3]
    print(H, is_max_heap(H))

    H = [None, 3, 1, 2]
    print(H, is_max_heap(H))