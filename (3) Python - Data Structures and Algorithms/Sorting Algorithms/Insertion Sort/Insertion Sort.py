def insertion_sort(items):
    items_len = len(items)

    for i in range(1, items_len):
        item = items[i]
        j = i - 1

        while j >= 0 and items[j] > item:
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = item


if __name__ == "__main__":
    array = [6, 1, 4, 9, 2]
    print("Before Sort: ", array)

    insertion_sort(array)
    print("After Insertion: ", array)
