import re

text = "Hello, my phone number is 1234567890."

print("Match:", re.match(r'Hello', text))
print("Search:", re.search(r'\d{10}', text))
print("Findall:", re.findall(r'\d+', text))