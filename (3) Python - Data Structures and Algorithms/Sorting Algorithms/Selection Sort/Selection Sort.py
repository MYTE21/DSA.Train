def selection_sort(items):
    items_len = len(items)

    for i in range(items_len - 1):
        min_index = i

        for j in range(i + 1, items_len):
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]


if __name__ == "__main__":
    array = [6, 1, 4, 9, 2]
    print("Before sort: ", array)

    selection_sort(array)
    print("After sort: ", array)
