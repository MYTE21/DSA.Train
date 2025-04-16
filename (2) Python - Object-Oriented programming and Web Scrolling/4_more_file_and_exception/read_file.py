import requests


with open("file.txt", "r") as file:
    content = file.read()

print(content)

# Read line by line
with open("file.txt", "r") as file:
    lines = file.readlines()

    i = 0
    for line in lines:
        print(f"({(i:= i + 1)}) {line}")


# Read line by line (2nd way)
with open("file.txt", "r") as file:
    for i, line in enumerate(file):
        print(f"({i + 1}) -> {line}")
