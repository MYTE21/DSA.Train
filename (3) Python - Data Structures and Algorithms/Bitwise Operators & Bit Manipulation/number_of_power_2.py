"""
Problem: How to check if a given number is a power of 2?
"""


def power_of_two(num: int) -> bool:
    if num == 0:
        return False

    while num % 2 == 0:
        num /= 2
    return True if num == 1 else False


if __name__ == '__main__':
    print(power_of_two(8))
