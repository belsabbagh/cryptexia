from cryptexia.ciphers.classic import Vernam

message = "HELLO"
key = "OCVHW"
encrypted = "HGAEY"


def test_encrypt():
    vernam = Vernam(key)
    assert vernam.encrypt(message) == encrypted


def test_decrypt():
    vernam = Vernam(key)
    assert vernam.decrypt(encrypted) == message
