from typing import List
import turtle


def fibonacci_generator(num: int) -> List[int]:
    fibonacci_list = [1, 1]

    i = 2
    while i < num:
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        i += 1

    return fibonacci_list


def fibonacci_circle(fibo_list: List[int]):
    colors: List[str] = ["red", "green",
                         "blue","yellow",
                         "orange", "purple"]

    base_radius: int = 5
    angle: int = 60

    turtle.left(90)
    for fibo_num in fibo_list:
        turtle.color(colors[fibo_num % 6])
        turtle.circle(fibo_num * base_radius, angle)

    turtle.done()


if __name__ == '__main__':
    number = int(input("Enter a number (for fibonacci): "))
    print(f"Generating Fibonacci numbers (1st to {number}th)...")
    fibonacci_numbers: List[int] = fibonacci_generator(number)
    print("Fibonacci numbers: ", fibonacci_numbers)
    fibonacci_circle(fibonacci_numbers)
