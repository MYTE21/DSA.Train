def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid type"


if __name__ == "__main__":
    print(div(10, 2))
    print(div(3, 0))
    print(div(9, 3))
    print(div("12", 3))
