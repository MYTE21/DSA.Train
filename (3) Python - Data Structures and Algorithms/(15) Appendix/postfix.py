def do_operation(operand_1, operand_2, operator):
    # if operator == "+":
    #     return int(operand_1) + int(operand_2)
    # elif operator == "-":
    #     return int(operand_1) - int(operand_2)
    # elif operator == "*":
    #     return int(operand_1) * int(operand_2)
    # else:
    #     return int(operand_1) / int(operand_2)
    return eval(operand_1 + operator + operand_2)


def postfix_evaluate(expression):
    operands = []
    operators = "*/_+"

    for character in expression:
        if character.isdigit():
            operands.append(character)
        elif character in operators:
            operand_2 = operands.pop()
            operand_1 = operands.pop()

            result = do_operation(operand_1, operand_2, character)
            operands.append(str(result))

    result = operands.pop()
    return int(result)


def test_postfix():
    test_cases = [
        {
            "input": "132*+",
            "expected": 7
        },
        {
            "input": "13+2*",
            "expected": 8
        },
        {
            "input": "13+24+*",
            "expected": 24
        },
        {
            "input": "132*+4+",
            "expected": 11
        },
        {
            "input": "13+2-",
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == postfix_evaluate(test_case["input"]), \
            f"Expected {test_case['expected']} but got {postfix_evaluate(test_case['input'])}"


if __name__ == "__main__":
    pass
