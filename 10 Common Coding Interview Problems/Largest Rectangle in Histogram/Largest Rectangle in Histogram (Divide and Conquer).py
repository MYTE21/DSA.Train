def largest_rectangle(heights: list[int]) -> int:
    return rectangle(heights, 0, len(heights) - 1)

def rectangle(heights: list[int], low: int, high: int) -> int:
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        min_height = min(heights[low:high+1])
        min_position = heights.index(min_height, low, high+1)
        left = rectangle(heights, low, min_position-1)
        right = rectangle(heights, min_position+1, high)
        return max(min_height*(high-low+1), left, right)


if __name__ == "__main__":
    try:
        assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10, (
            "1. ⚠️ The largest rectangle area for the [2, 1, 5, 6, 2, 3] histogram should be 10!"
        )
        assert largest_rectangle([2, 4]) == 4, (
            "2. ⚠️ The largest rectangle area for the [2, 4] histogram should be 4!"
        )
        print("✅ All tests passed!")
    except AssertionError as e:
        print(f"❌ Test Failed: \n{e}")
