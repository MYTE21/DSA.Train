def is_balanced_brackets(input_brackets):
    store = []

    for b in input_brackets:
        if b in "({[":
            store.append(b)
        if b in ")}]":
            if not store:
                return False
            elif b == ")" and store[-1] != "(":
                return False
            elif b == "}" and store[-1] != "{":
                return False
            elif b == "]" and store[-1] != "[":
                return False
            else:
                store.pop()

    return not store


if __name__ == "__main__":
    brackets_list = ["{{([])}}", "[{{{[)}}"]

    for b_str in brackets_list:
        if is_balanced_brackets(b_str):
            print(f"{b_str} is balanced ...!")
        else:
            print(f"{b_str} is not balanced ...!")
