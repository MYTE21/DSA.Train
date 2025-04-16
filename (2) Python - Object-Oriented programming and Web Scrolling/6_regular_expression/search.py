import re


match = re.search("Bangla", "Bangladesh")

print(match)
print(match.group())


s = "Bangladesh"

match = re.search(".", s)
print(match.group())

match = re.search("B.n", s)
print(match.group())

match = re.search("B.n...", s)
print(match.group())

s = "Bangladesh is our homeland."
match = re.search("............", s)
print(match.group())

# Only words and character
s = "Bangladesh is our homeland."
match = re.search(r"o\w\w", s)
print(match.group())

match = re.search(r"i\w\w", s)
print(match)

match = re.search(r"B\w+h", s)
print(match.group())

match = re.search(r"B.+h", s)
print(match.group())

match = re.search(r"B.+?h", s)
print(match.group())

text = "Phone number: 01711101001."
match = re.search(r"\d+", text)
print(match.group())

text = "House number: 5, Phone number: 01711101001."
match = re.search(r"\d+", text)
print(match.group())

match = re.search(r"\d{11}", text)
print(match.group())

text = "House number: 5, Phone number: 017 11101001."
match = re.search(r"\d{3}\s*\d{8}", text)
print(match.group())


text = "House number: 5, Phone number: 017 11101001."
match = re.search(r"\d{3}\s?\d{8}", text)
print(match.group())

text = "Multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000, 123-123"
match = re.findall(r"\d{3}\s?\d{8}", text)
print(match)

match = re.findall(r"01[56789]\s?\d{8}", text)
print(match)

print("#"*50)

s = "Bangla english bangla"
print(re.findall(r"english", s))
print(re.findall(r"^english", s))
print(re.findall(r"english$", s))
print(re.findall(r"^Bangla", s))
print(re.findall(r"bangla$", s))

print("#"*50)

print(re.findall(r"^bangla", s, re.IGNORECASE))
print(re.findall(r"Bangla$", s, re.I))
