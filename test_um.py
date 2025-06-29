from um import count

def test_one_um():
    assert count("um") == 1

def test_um_with_punctuation():
    assert count("Um, thanks for the album.") == 1

def test_multiple_ums():
    assert count("Um, thanks, um...") == 2

def test_no_um():
    assert count("yummy umm umbrella") == 0
