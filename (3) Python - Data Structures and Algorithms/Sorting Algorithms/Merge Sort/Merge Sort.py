def merge(left_items, right_items):
    merged_items = []

    len_left_items, len_right_items = len(left_items), len(right_items)
    index_left_item, index_right_item = 0, 0

    while (index_left_item < len_left_items) and (index_right_item < len_right_items):
        if left_items[index_left_item] < right_items[index_right_item]:
            merged_items.append(left_items[index_left_item])
            index_left_item += 1
        else:
            merged_items.append(right_items[index_right_item])
            index_right_item += 1

    if index_left_item < len_left_items:
        merged_items.extend(left_items[index_left_item:])
    elif index_right_item < len_right_items:
        merged_items.extend(right_items[index_right_item:])

    return merged_items


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


if __name__ == "__main__":
    arrays = [
        [4, 7, 2, 3],
        [10],
        [10, 9, 8, 7, 6],
        [2, 3, 1],
        [1, 2],
        [2, 1]
    ]

    for array in arrays:
        sorted_array = merge_sort(array)

        print("Original array: ", array)
        print("Sorted array: ", sorted_array, "\n")
