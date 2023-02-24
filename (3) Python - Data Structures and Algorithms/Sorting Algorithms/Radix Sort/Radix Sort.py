"""
    YouTube Resource: https://www.youtube.com/watch?v=BVGRgTALQ44
    GitHub Resource: https://github.com/joeyajames/Python/blob/master/Sorting%20Algorithms/Radix_Sort.ipynb
"""
from functools import reduce


def max_item_digits(items):
    max_item = max(items)
    max_item_len = len(str(max_item))
    return max_item_len


def flatten(items):
    return reduce(lambda x, y: x + y, items)


def radix_sort(items):
    num_digits = max_item_digits(items)

    for digit in range(num_digits):
        bucket = [[] for i in range(10)]

        for item in items:
            num = (item // (10 ** digit)) % 10
            bucket[num].append(item)

        items = flatten(bucket)

    return items


if __name__ == "__main__":
    array = [121, 432, 564, 23, 1, 45, 788]
    print("Before sorting: ", array)

    sorted_array = radix_sort(array)
    print("After sorting: ", sorted_array)
