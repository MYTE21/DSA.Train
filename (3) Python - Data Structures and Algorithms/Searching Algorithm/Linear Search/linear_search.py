def linear_search(items, search_item):
    items_len = len(items)

    for i in range(items_len):
        if items[i] == search_item:
            return i

    return -1


if __name__ == "__main__":
    array = [2, 4, 0, 1, 9]
    search = 1

    result = linear_search(array, search)

    print("Element not found ...!") if result == -1 else print("Element found at index ", result)
