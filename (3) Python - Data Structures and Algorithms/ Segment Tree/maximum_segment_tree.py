"""
Tutorial Link: https://youtu.be/-dUiRtJ8ot0?si=C3sKYeDL43C_Vqww
"""
def build(arr: list[int], tree: list[int | float], index: int, low: int, high: int) -> None:
    """
    Recursively build the segment tree for range maximum query.
    """
    if low == high:
        tree[index] = arr[low]
        return

    mid = (low + high) // 2

    # Build left and right subtrees
    build(arr, tree, 2 * index + 1, low, mid)
    build(arr, tree, 2 * index + 2, mid + 1, high)

    # Internal node stores maximum of children
    tree[index] = max(tree[2 * index + 1], tree[2 * index + 2])


def query(tree: list[int | float], index: int, low: int, high: int,
          left: int, right: int) -> int | float:
    """
    Perform range maximum query for interval [left, right].
    """

    # Complete overlap
    if left <= low and high <= right:
        return tree[index]

    # No overlap
    if high < left or low > right:
        return float("-inf")

    # Partial overlap
    mid = (low + high) // 2

    left_max = query(tree, 2 * index + 1, low, mid, left, right)
    right_max = query(tree, 2 * index + 2, mid + 1, high, left, right)

    return max(left_max, right_max)


if __name__ == "__main__":

    numbers = [8, 2, 5, 1, 4, 7, 3, 9, 6, 10]
    ranges = [[1, 2], [2, 5], [4, 8]]

    n = len(numbers)

    # Allocate tree (4 * n is safe size)
    segment_tree = [float("-inf")] * (4 * n)
    print("S: ", segment_tree[0])

    # Build tree
    build(numbers, segment_tree, 0, 0, n - 1)

    # Perform queries
    for left_item, right_item in ranges:
        if 0 <= left_item <= right_item < n:
            result = query(segment_tree, 0, 0, n - 1, left_item, right_item)
            print(f"Max in range [{left_item}, {right_item}] = {result}")
        else:
            print(f"Invalid range: [{left_item}, {right_item}]")
