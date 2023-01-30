def partition(items, low, high):
    pivot = items[high]

    i = low - 1

    for j in range(low, high):
        if items[j] < pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1


def quick_sort(items, low, high):
    if low >= high:
        return

    p = partition(items, low, high)

    quick_sort(items, low, p - 1)
    quick_sort(items, p + 1, high)


if __name__ == "__main__":
    array = [1, 5, 6, 3, 8, 4, 7, 2]
    print("Before sorting: ", array)

    quick_sort(array, 0, len(array) - 1)
    print("After sorting: ", array)
