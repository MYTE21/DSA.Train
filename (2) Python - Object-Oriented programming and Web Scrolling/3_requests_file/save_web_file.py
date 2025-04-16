import requests
import os
import webbrowser as wb


url = "https://www.gettingstarted.ai/"

response = requests.get(url)

with open("ai.html", "w") as file:
    file.write(response.text)

file_path = os.path.realpath("ai.html")
print("File Path: ", file_path)

wb.open("file://" + file_path)
