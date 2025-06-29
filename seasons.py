from datetime import date, datetime
import sys
import inflect

def main():
    birthdate_str = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    except ValueError:
        sys.exit("Invalid date format")

    minutes = calculate_minutes(birthdate)
    words = convert_to_words(minutes)
    print(words.capitalize() + " minutes")

def calculate_minutes(birthdate):
    today = date.today()
    delta = today - birthdate
    return delta.days * 24 * 60

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")

if __name__ == "__main__":
    main()

