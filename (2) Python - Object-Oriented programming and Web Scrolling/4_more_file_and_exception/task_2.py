import requests
import os


with open("country.txt", "r") as file:
    countries = file.readlines()

for country in countries:
    os.makedirs("countries", exist_ok=True)
    file_path = os.path.join("countries",  country[0] + ".txt")
    print(file_path)

    with open(file_path, "a") as file:
        file.write(country)