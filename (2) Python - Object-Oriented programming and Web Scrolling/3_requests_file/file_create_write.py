# fp = open("test.txt", "w")
# fp.write("Hello..!")
# fp.close()
#
# print(type(fp))
# print(fp)

with open("test.txt", "w") as file:
    file.write("Hello, Python ..!\n")

print(file)
