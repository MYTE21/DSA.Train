from typing import List
import timeit


def prime_numbers(num_1: int, num_2: int) -> List[int]:
    primes = []

    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    for num in range(num_1, num_2 + 1):
        if num == 2:
            primes.append(num)
        if num < 2 or not num % 2:
            continue

        is_prime = True
        start = 3
        end = num // 2 + 1

        for i in range(start, end, 2):
            if not num % i:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


if __name__ == '__main__':
    number_1 = int(input("1st number: "))
    number_2 = int(input("2nd number: "))

    print(f"Prime numbers from {number_1} to {number_2} are: {prime_numbers(number_1, number_2)}")
