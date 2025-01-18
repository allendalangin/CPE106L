def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        mid = n // 2
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[n // 2]

def mode(numbers):
    from collections import Counter
    counts = Counter(numbers)
    max_count = max(counts.values())
    mode_list = [num for num, count in counts.items() if count == max_count]
    return mode_list[0] if mode_list else None
