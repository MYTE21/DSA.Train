def infix_to_postfix(expression):
    precedence = {
        "/": 2,
        "*": 2,
        "-": 1,
        "+": 1
    }

    operators = "*/-+"
    operators_stack = []
    postfix = []

    for item in expression:
        if item.isdigit():
            postfix.append(item)
        elif item in operators:
            while operators_stack:
                op = operators_stack.pop()
                if precedence[op] >= precedence[item]:
                    postfix.append(op)
                else:
                    operators_stack.append(op)
                    break
            operators_stack.append(item)

    while operators_stack:
        op = operators_stack.pop()
        postfix.append(op)

    return " ".join(postfix)


if __name__ == "__main__":
    input_expression = "1 + 2 + 3 * 4 - 5"
    postfix_expression = infix_to_postfix(input_expression)
    print(postfix_expression)
