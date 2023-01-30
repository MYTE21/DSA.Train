# ! Can't solve the problem
# TODO: It should be solved
def possible_subsets(array, array_len):
    for i in range(0, (1 << array_len)):
        for j in range(0, array_len):
            if i & (1 << j):
                print(array[j], end=" ")

        print()


if __name__ == "__main__":
    element = ["a", "b" "c"]
    ele_len = len(element)

    possible_subsets(element, ele_len)