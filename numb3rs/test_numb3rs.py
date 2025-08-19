from numb3rs.numb3rs import validate
def test_valid_address():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True
def test_invalid_numbers():
    assert validate("00.0.0.0") == False
    assert validate("255.255.255.256") == False
    assert validate("192.368.1.1") == False
def test_wrong_format():
    assert validate("0.0.0.0.0") == False
    assert validate("255.255.255.255.") == False
    assert validate("192..168.1.1") == False
