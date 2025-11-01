import file_tools as ft
import os

def create_test_file(filename, content):
    """Helper function to create a test file"""
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def main():
    print("=== File Tools Demo ===\n")
    
    # Create a test file
    test_content = """Hello, this is a test file.
It contains multiple lines of text.
Some lines are longer than others.
The quick brown fox jumps over the lazy dog.
Python is an amazing programming language!"""
    
    test_file = "test_document.txt"
    create_test_file(test_file, test_content)
    print(f"1. Created test file: {test_file}")
    
    # Test file statistics
    try:
        lines, words, chars = ft.count_file_stats(test_file)
        print("\n2. File Statistics:")
        print(f"   Lines: {lines}")
        print(f"   Words: {words}")
        print(f"   Characters: {chars}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test with a non-existent file
    non_existent = "non_existent_file.txt"
    print(f"\n3. Testing with non-existent file ({non_existent}):")
    lines, words, chars = ft.count_file_stats(non_existent)
    print(f"   Lines: {lines}, Words: {words}, Characters: {chars}")
    
    # Test with an empty file
    empty_file = "empty_file.txt"
    create_test_file(empty_file, "")
    print(f"\n4. Testing with empty file ({empty_file}):")
    lines, words, chars = ft.count_file_stats(empty_file)
    print(f"   Lines: {lines}, Words: {words}, Characters: {chars}")
    
    # Test with a file containing only whitespace
    whitespace_file = "whitespace.txt"
    create_test_file(whitespace_file, "   \n  \t  \n    ")
    print(f"\n5. Testing with whitespace-only file (whitespace.txt):")
    lines, words, chars = ft.count_file_stats(whitespace_file)
    print(f"   Lines: {lines}, Words: {words}, Characters: {chars}")
    
    # Test with a large file
    print("\n6. Testing with a larger file (lorem_ipsum.txt):")
    lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nullam auctor, nisl eget ultricies tincidunt, nunc nisl aliquam nunc,
vitae aliquam nisl nunc vitae nisl. Sed vitae nisl eget nunc."""
    
    large_file = "lorem_ipsum.txt"
    create_test_file(large_file, lorem_ipsum)
    lines, words, chars = ft.count_file_stats(large_file)
    print(f"   Lines: {lines}, Words: {words}, Characters: {chars}")
    
    # Clean up test files
    print("\n7. Cleaning up test files...")
    for f in [test_file, empty_file, whitespace_file, large_file]:
        if os.path.exists(f):
            os.remove(f)
            print(f"   Deleted: {f}")
    
    # Example of using the function in a real-world scenario
    print("\n8. Example: Analyzing a Python file")
    current_file = os.path.basename(__file__)
    try:
        lines, words, chars = ft.count_file_stats(current_file)
        print(f"   File: {current_file}")
        print(f"   Lines: {lines}, Words: {words}, Characters: {chars}")
    except Exception as e:
        print(f"   Could not analyze {current_file}: {e}")
    
    # Example of checking multiple files
    print("\n9. Checking multiple files in current directory:")
    file_list = [f for f in os.listdir() if f.endswith('.py') and os.path.isfile(f)]
    for idx, filename in enumerate(file_list[:3], 1):  # Show first 3 .py files
        try:
            lines, words, chars = ft.count_file_stats(filename)
            print(f"   {idx}. {filename}: {lines} lines, {words} words, {chars} chars")
        except Exception as e:
            print(f"   {idx}. {filename}: Error - {e}")
    if len(file_list) > 3:
        print(f"   ... and {len(file_list) - 3} more files")

if __name__ == "__main__":
    main()
