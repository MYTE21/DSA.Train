from typing import List


def square_list_generator(num_list: List[int]) -> List[int]:
    square_list: List[int] = [x ** 2 for x in num_list]
    return square_list


if __name__ == "__main__":
    li: List[int] = [1, 2, 3, 4, 5]
    print(square_list_generator(li))
