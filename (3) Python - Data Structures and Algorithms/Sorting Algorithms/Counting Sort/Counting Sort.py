def counting_sort(items):
    count = [0] * (max(items) + 1)
    for item in items:
        count[item] += 1

    sorted_items = []
    for index, value in enumerate(count):
        if value > 0:
            sorted_items.extend([index] * value)

    return sorted_items


if __name__ == "__main__":
    array = [3, 4, 1, 6, 2, 4, 9, 7, 8, 4, 2, 1]
    print("Before sorting: ", array)

    sorted_array = counting_sort(array)
    print("After sorting: ", sorted_array)
