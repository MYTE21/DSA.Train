""" InterviewBit
    Difficulty: Medium
    - Max Distance
    - Problem Link: https://www.interviewbit.com/problems/max-distance/
"""


def maximum_gap(a):
    numbers = []
    for i, num in enumerate(a):
        numbers.append((num, i))

    numbers.sort()

    max_gap = 0
    min_number = numbers[0][1]

    for item in numbers:
        num = item[1]
        if num <= min_number:
            min_number = num
        else:
            max_gap = max(max_gap, num - min_number)

    return max_gap


if __name__ == "__main__":
    nums = [3, 5, 4, 2]
    print(maximum_gap(nums))
