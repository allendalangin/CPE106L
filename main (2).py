def main():
    # Prompt the user for the filename
    try:
        filename = input("Enter the filename: ")
        
        # Open the file and read all lines into a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Remove trailing whitespace (like newlines) from each line
        lines = [line.rstrip() for line in lines]

        # Enter the navigation loop
        while True:
            print(f"\nThe file has {len(lines)} lines.")
            print("Enter a line number to view (0 to quit): ")
            try:
                # Prompt for a line number
                line_number = int(input("Line number: "))
                
                if line_number == 0:
                    print("Exiting the program.")
                    break
                elif 1 <= line_number <= len(lines):
                    # Print the requested line
                    print(f"Line {line_number}: {lines[line_number - 1]}")
                else:
                    print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")
            except ValueError:
                print("Please enter a valid number.")

    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure the file exists.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
