import requests


# url = "https://medium.com"
url = "https://medium.com/myte"

response = requests.get(url)

print("Type: ", type(response))
print(dir(response))

print(response.ok)
print(response.status_code)
print(response.reason)

res = requests.get("https://example.com")
print(res.ok)
print(res.text)
print(type(res.text))