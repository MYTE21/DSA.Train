def binary_upper_bound(items, search_item):
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] <= search_item:
            left = mid + 1
        else:
            right = mid - 1

    return right if (0 <= right < len(items)) and (items[right] == search_item) else -1


if __name__ == "__main__":
    array = [1, 2, 3, 3, 3, 4, 5]
    search = 3

    ans = binary_upper_bound(array, search)
    print(ans)
