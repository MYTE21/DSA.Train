import requests


text = "This is first line.\nThis is second line.\nThis is third line."

with open("file.txt", "w") as file:
    file.write(text)
