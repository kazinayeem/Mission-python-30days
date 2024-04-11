import re


def main():
    # Example 1: Matching a simple pattern
    text = "Hello, world! This is a sample text with some numbers 12345 and special characters #@!."
    pattern1 = r'world'
    matches1 = re.findall(pattern1, text)
    print("Example 1 - Matching 'world':", matches1)

    # Example 2: Matching multiple occurrences of a pattern
    pattern2 = r'\d+'
    matches2 = re.findall(pattern2, text)
    print("Example 2 - Matching numbers:", matches2)

    # Example 3: Using groups to extract specific parts of a pattern
    pattern3 = r'(\w+), (\w+)!'
    match3 = re.search(pattern3, text)
    if match3:
        print("Example 3 - Extracting 'Hello' and 'world':")
        print("Full match:", match3.group(0))
        print("First group:", match3.group(1))
        print("Second group:", match3.group(2))

    # Example 4: Finding all occurrences of a pattern with start and end positions
    pattern4 = r'is'
    for match in re.finditer(pattern4, text):
        print("Example 4 - Finding all occurrences of 'is':")
        print("Found 'is' at position:", match.start())

    # Example 5: Replacing a pattern with a different string
    pattern5 = r'[!@#]'
    replaced_text = re.sub(pattern5, '', text)
    print("Example 5 - Replacing special characters:", replaced_text)


if __name__ == "__main__":
    main()
