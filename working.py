import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex pattern to match all allowed formats
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    h1, m1, am_pm1, h2, m2, am_pm2 = match.groups()

    # Default to 00 minutes if not present
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0

    h1 = int(h1)
    h2 = int(h2)

    # Validate hours and minutes
    if not (1 <= h1 <= 12) or not (0 <= m1 <= 59):
        raise ValueError("Invalid start time")
    if not (1 <= h2 <= 12) or not (0 <= m2 <= 59):
        raise ValueError("Invalid end time")

    # Convert start time
    if am_pm1 == "AM":
        h1 = 0 if h1 == 12 else h1
    else:
        h1 = h1 if h1 == 12 else h1 + 12

    # Convert end time
    if am_pm2 == "AM":
        h2 = 0 if h2 == 12 else h2
    else:
        h2 = h2 if h2 == 12 else h2 + 12

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
