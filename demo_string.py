import string_ops as so

text = "A man, a plan, a canal: Panama"
print(f"Vowels in '{text}': {so.count_vowels(text)}")
print(f"Reversed: '{so.reverse_string(text)}'")
print(f"Is palindrome? {so.is_palindrome(text)}")
