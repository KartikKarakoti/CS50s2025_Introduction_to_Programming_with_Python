from seasons import calculate_minutes, convert_to_words
from datetime import date, timedelta

def test_calculate_minutes():
    today = date.today()
    one_day_ago = today - timedelta(days=1)
    assert calculate_minutes(one_day_ago) == 1440

def test_convert_to_words():
    assert convert_to_words(1440) == "one thousand four hundred forty"
    assert convert_to_words(525600) == "five hundred twenty-five thousand six hundred"
