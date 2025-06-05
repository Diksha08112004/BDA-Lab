import re

email = "user@example.com"
phone = "9876543210"
ssn = "123-45-6789"

print("Valid Email:", bool(re.fullmatch(r'\w+@\w+\.\w+', email)))
print("Valid Phone:", bool(re.fullmatch(r'\d{10}', phone)))
print("Valid SSN:", bool(re.fullmatch(r'\d{3}-\d{2}-\d{4}', ssn)))