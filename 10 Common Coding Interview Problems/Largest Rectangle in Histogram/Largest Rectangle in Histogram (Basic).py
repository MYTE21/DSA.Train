def largest_rectangle(heights: list[int]) -> int:
    max_area = 0

    for i in range(len(heights)):
        left = i
        while left - 1 >= 0 and heights[left - 1] >= heights[i]:
            left -= 1

        right = i
        while right + 1 < len(heights) and heights[right + 1] >= heights[i]:
            right += 1

        width = right - left + 1
        area = width * heights[i]

        max_area = max(max_area, area)

    return max_area


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
