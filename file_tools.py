def count_file_stats(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.count('\n') + 1
            words = len(content.split())
            chars = len(content)
            return lines, words, chars
    except FileNotFoundError:
        return 0, 0, 0
