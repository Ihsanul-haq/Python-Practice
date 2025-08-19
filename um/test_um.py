from um.um import count
def test_lowercase():
    assert count("um") == 1
    assert count("um, hi") == 1
    assert count("hi, um, hi") == 1
def test_uppercase():
    assert count("UM, thanks") == 1
    assert count("Um") == 1
def test_mixed():
    assert count("um uM UM Um") == 4
def test_in_words():
    assert count("umhello yummy, umbrella") == 0