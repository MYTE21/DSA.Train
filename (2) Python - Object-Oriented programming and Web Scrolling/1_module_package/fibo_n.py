def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
        fib_x, fib_next = fib_next, fib_x + fib_next
        i += 1

    return fib_next


def list_fib(n):
    fib_list = []

    for i in range(0, n + 1):
        fib_list.append(find_fib(i))

    return fib_list


if __name__ == "__main__":
    print("Fibonacci: ")
    for x in range(1, 11):
        fib = find_fib(x)
        print("Fibonacci number", x, "is: ", fib)

    print("\nFibonacci List: ")
    print(list_fib(10))
