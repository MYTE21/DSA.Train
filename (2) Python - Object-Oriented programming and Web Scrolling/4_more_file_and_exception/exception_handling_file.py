import io


file_name = "file.txt"
mode = "r"

try:
    with open(file_name, mode) as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{file_name} not found..!")
except io.UnsupportedOperation:
    print(f"{file_name} not readable..!")
    