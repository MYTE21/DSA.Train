from functools import reduce


def bucket_sort(items):
    bucket = [[] for i in range(len(items))]

    for item in items:
        index = int(item * 10)
        bucket[index].append(item)

    for i in range(len(items)):
        bucket[i] = sorted(bucket[i])

    items = reduce(lambda x, y: x + y, bucket)

    return items


if __name__ == "__main__":
    array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Before sorting: ", array)

    sorted_array = bucket_sort(array)
    print("After sorting: ", sorted_array)
