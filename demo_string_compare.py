import string_compare as sc

def main():
    print("=== String Comparison Demo ===\n")
    
    # Example 1: Basic comparison
    str1 = "apple"
    str2 = "banana"
    print(f"1. Comparing '{str1}' and '{str2}': {sc.compare_strings(str1, str2)}")
    
    # Example 2: Case sensitivity
    str3 = "Apple"
    print(f"\n2. Comparing '{str1}' and '{str3}': {sc.compare_strings(str1, str3)}")
    
    # Example 3: Identical strings
    str4 = "apple"
    print(f"\n3. Comparing '{str1}' and '{str4}': {sc.compare_strings(str1, str4)}")
    
    # Example 4: Empty strings
    empty_str = ""
    print(f"\n4. Comparing '{str1}' and empty string: {sc.compare_strings(str1, empty_str)}")
    print(f"   Comparing empty strings: {sc.compare_strings(empty_str, empty_str)}")
    
    # Example 5: Numeric strings
    num1 = "100"
    num2 = "20"
    print(f"\n5. Comparing '{num1}' and '{num2}': {sc.compare_strings(num1, num2)}")
    
    # Example 6: Special characters
    special1 = "hello!"
    special2 = "hello?"
    print(f"\n6. Comparing '{special1}' and '{special2}': {sc.compare_strings(special1, special2)}")
    
    # Example 7: String with spaces
    spaced1 = "hello world"
    spaced2 = "hello"
    print(f"\n7. Comparing '{spaced1}' and '{spaced2}': {sc.compare_strings(spaced1, spaced2)}")
    
    # Example 8: Long strings
    long1 = "The quick brown fox"
    long2 = "The quick brown dog"
    print(f"\n8. Comparing long strings: {sc.compare_strings(long1, long2)}")
    
    # Example 9: Case-insensitive comparison
    def case_insensitive_compare(str1, str2):
        return sc.compare_strings(str1.lower(), str2.lower())
    
    case1 = "Python"
    case2 = "python"
    print(f"\n9. Case-insensitive comparison of '{case1}' and '{case2}': {case_insensitive_compare(case1, case2)}")
    
    # Example 10: String similarity percentage
    def string_similarity(str1, str2):
        if str1 == str2:
            return 100.0
        
        # Count matching characters
        matches = sum(1 for a, b in zip(str1, str2) if a == b)
        
        # Calculate similarity percentage
        max_len = max(len(str1), len(str2))
        return (matches / max_len) * 100 if max_len > 0 else 0
    
    word1 = "kitten"
    word2 = "sitting"
    similarity = string_similarity(word1, word2)
    print(f"\n10. Similarity between '{word1}' and '{word2}': {similarity:.1f}%")

if __name__ == "__main__":
    main()
