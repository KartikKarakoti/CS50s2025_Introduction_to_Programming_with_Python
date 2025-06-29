import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # \bum\b matches "um" as a whole word (word boundaries)
    # re.IGNORECASE makes it case-insensitive
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()
