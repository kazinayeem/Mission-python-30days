# Day 17: Regular Expressions

import re


def main():
    # Example 1: Matching a pattern
    text = "The quick brown fox jumps over the lazy dog"
    pattern = r"fox"
    match = re.search(pattern, text)
    if match:
        print("Pattern found:", match.group())
    else:
        print("Pattern not found")

    # Example 2: Matching multiple patterns
    text = "Emails: user1@example.com, user2@example.com, user3@example.com"
    pattern = r"\w+@\w+\.\w+"
    matches = re.findall(pattern, text)
    print("Emails found:", matches)

    # Example 3: Substitution
    text = "Hello, World!"
    pattern = r"World"
    new_text = re.sub(pattern, "Python", text)
    print("New text:", new_text)

    # Example 4: Splitting text
    text = "The quick-brown-fox"
    pattern = r"[-\s]"  # Split by hyphen or space
    parts = re.split(pattern, text)
    print("Split parts:", parts)


if __name__ == "__main__":
    main()
