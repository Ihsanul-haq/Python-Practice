from test_bank.bank import value
def test_hello():
    assert value("hello") == 0
    assert value("Hello there") == 0
    assert value("  hello, sir") == 0

def test_h():
    assert value("hey") == 20
    assert value("Hi you") == 20
    assert value("  hmmm") == 20

def test_other():
    assert value("good bye") == 100
    assert value("what's up") == 100
    assert value(" no greeting") == 100

