def compare_strings(str1, str2):
    if str1 < str2:
        return f"'{str1}' comes before '{str2}'"
    elif str1 > str2:
        return f"'{str1}' comes after '{str2}'"
    else:
        return "The strings are identical"
