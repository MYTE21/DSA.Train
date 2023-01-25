def binary_search(items, search_item):
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == search_item:
            return mid

        if items[mid] < search_item:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    array = [1, 2, 3, 5, 6, 7, 8, 9]

    for num in range(1, 11):
        position = binary_search(array, num)

        if position == -1:
            if num in array:
                print(f"{num} is in {array}, but function returned -1 ..!")
            else:
                print(f"{num} not in list ..!")
        else:
            if array[position] == num:
                print(f"{num} found in correct position..!")
            else:
                print(f"Binary Search returned {position} for {num} which is incorrect..!")

    print("Program Terminated..!")
