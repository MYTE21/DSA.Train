""" InterviewBit
    Difficulty: Medium
    - Maximum Unsorted Subarray
    - Problem Link: https://www.interviewbit.com/problems/maximum-unsorted-subarray/
"""


def max_unsorted_subarray(array):
    length = len(array)
    given_array = array
    array.sort()
    sorted_array = array
    first_point = -1
    second_point = -1

    for i in range(length):
        if given_array[i] != sorted_array[i]:
            if first_point == -1:
                first_point = i

    return [first_point, second_point]


if __name__ == "__main__":
    """ Time Complexity
        - 
    """
    arrays = [
        [1, 3, 2, 4, 5],
        [1, 4, 2, 3, 5],
        [1, 2, 3, 4, 5],
        [3, 2, 1],
        [5, 6, 1, 2, 4, 7]
    ]
    for items in arrays:
        print(max_unsorted_subarray(items))