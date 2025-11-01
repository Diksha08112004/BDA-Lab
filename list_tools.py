def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_smallest(numbers):
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
