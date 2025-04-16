import requests

url = "https://goo.gl/JxktPw"

response = requests.get(url)

with open("pybook.png", "wb") as file:
    file.write(response.content)
