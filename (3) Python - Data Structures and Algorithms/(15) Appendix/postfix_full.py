def do_operation(operand_1, operand_2, operator):
    return eval(operand_1 + operator + operand_2)


def postfix_evaluate_full(expression):
    operands = []
    operators = ["*", "/", "-", "+"]

    expression_list = expression.split(",")

    for item in expression_list:
        if item in operators:
            operand_2 = operands.pop()
            operand_1 = operands.pop()
            result = do_operation(operand_1, operand_2, item)
            operands.append(str(result))
        else:
            operands.append(item)

    result = operands.pop()
    return result


if __name__ == "__main__":
    math_expression = "20,30,+,2,*,10,*,4,/"
    ans = postfix_evaluate_full(math_expression)
    print(ans)
