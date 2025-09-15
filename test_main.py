from main import kiwi

def test_kiwi_number():
    assert(kiwi(4) == 4)

def test_kiwi_letter():
    assert(kiwi('m') == "not an Int")

def test_kiwi_float():
    assert(kiwi(4.2) == "not an Int")

