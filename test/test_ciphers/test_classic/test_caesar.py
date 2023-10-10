from cryptexia.ciphers.classic import Caesar


def test_encrypt():
    method = Caesar(3)
    res = method.encrypt("ABC")
    assert res == "DEF"


def test_decrypt():
    method = Caesar(3)
    res = method.decrypt("DEF")
    assert res == "ABC"
