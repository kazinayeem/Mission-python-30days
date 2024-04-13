import re

# Define a function to read a text file and return its content
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return None

# Define a function to search for a pattern in the text using regular expressions
def search_pattern(text, pattern):
    return re.findall(pattern, text)

# Define a function to perform some operations on the extracted data using functional programming
def process_data(data):
    return list(map(lambda x: x.upper(), data))

# Main function to orchestrate the program
def main():
    # Read the contents of a text file
    file_content = read_file('sample_text.txt')

    if file_content:
        # Define your regular expression pattern
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Email pattern as an example

        # Search for patterns in the text
        matches = search_pattern(file_content, pattern)

        if matches:
            # Process the extracted data using functional programming
            processed_data = process_data(matches)

            # Print or do something with the processed data
            print("Processed data:", processed_data)
        else:
            print("No matches found.")
    else:
        print("Unable to process file content.")

if __name__ == "__main__":
    main()
