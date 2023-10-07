from cryptexia.ciphers.classic import Vernam

message = "HELLO"


def test_encrypt():
    vernam = Vernam()
    res = vernam.encrypt(message)[1]
    assert len(res) == len(message)


def test_decrypt():
    vernam = Vernam()
    cipher, key = vernam.encrypt(message)
    assert len(cipher) == len(message) == len(key)
    decrypted = vernam.decrypt(cipher, key)
    assert decrypted == message
