def is_balanced_parentheses(input_parentheses):
    store = []

    for p in input_parentheses:
        if p == "(":
            store.append(p)
        if p == ")":
            if not store:
                return False
            store.pop()

    return not store


if __name__ == "__main__":
    parentheses_list = ["(", ")", "()", ")(", "((())", "((()))", "()()()", "()())("]

    for p_str in parentheses_list:
        if is_balanced_parentheses(p_str):
            print(f"{p_str} is balanced...!")
        else:
            print(f"{p_str} is not balanced...!")
