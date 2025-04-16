import sys
import requests


image_url = sys.argv[1]
file_name = sys.argv[2]

response = requests.get(image_url)

print(sys.argv)

with open(file_name, "wb") as file:
    file.write(response.content)
