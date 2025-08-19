from working import convert
def test_format():
    assert convert("5 AM to 11 AM") == "05:00 to 11:00"
    assert convert("5:00 AM to 2:00 PM") == "05:00 to 14:00"