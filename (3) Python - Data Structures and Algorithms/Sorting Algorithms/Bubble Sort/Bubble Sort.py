def bubble_sort(items):
    items_len = len(items)

    for i in range(items_len):
        for j in range(items_len - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]


if __name__ == "__main__":
    array = [6, 1, 4, 9, 2]
    print("Before sort: ", array)

    bubble_sort(array)
    print("After sort: ", array)
