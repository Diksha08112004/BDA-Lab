import re

text = "My email is test@example.com and phone is 9876543210"
pattern = r'\w+@\w+\.\w+'
matches = re.findall(pattern, text)
print("Email found:", matches)