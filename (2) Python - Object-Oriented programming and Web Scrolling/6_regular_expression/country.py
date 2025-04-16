string = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"

countries = string.split(",")
print("Countries: ", countries)

countries_ends_with_land = [country for country in countries if country.endswith("land") or country.endswith("lands")]
print("Countries ends with land: ", countries_ends_with_land)


# Regular Expression
import re

countries = re.findall(r"(\w+lands*)", string)
print("Countries (Regular Expression): ", countries)