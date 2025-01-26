from collections import Counter

def mean(numbers):
    """Compute the mean (average) of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:
        # If even, median is the average of the two middle numbers
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        # If odd, median is the middle number
        return sorted_numbers[mid]

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:
        return 0
    count = Counter(numbers)
    max_count = max(count.values())

    # Get all modes (there might be ties)
    modes = [num for num, freq in count.items() if freq == max_count]

    if len(modes) == 1:
        return modes[0]  # Single mode
    else:
        return modes  # Return list of modes if there's a tie

def read_numbers_from_file(file_name):
    """Read numbers from a file and return them as a list."""
    numbers = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    numbers.append(float(word))
    except Exception as e:
        print(f"Error reading file: {e}")
    return numbers

def main():
    """Test the mean, median, and mode functions with a file input."""
    file_name = input("Enter the file name: ")
    numbers = read_numbers_from_file(file_name)

    if not numbers:
        print("The file is empty or contains invalid data.")
        return

    print("Numbers from file:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()
