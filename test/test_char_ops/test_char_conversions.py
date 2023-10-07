from cryptexia.char_ops import ascii2int, int2ascii, char2int, int2char


def test_ascii2int():
    assert ascii2int(65) == 0
    assert ascii2int(90) == 25


def test_int2ascii():
    assert int2ascii(0) == "A"
    assert int2ascii(25) == "Z"


def test_char2int():
    assert char2int("A") == 0
    assert char2int("Z") == 25


def test_int2char():
    assert int2char(0) == "A"
    assert int2char(25) == "Z"
