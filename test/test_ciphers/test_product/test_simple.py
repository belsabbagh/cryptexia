from cryptexia.ciphers.product import ProductCipher
from cryptexia.ciphers.classic import Caesar, Vigenere

message = "abc".upper()
key = "key".upper()
ciphertext = "nid".upper()

ciphers = [Caesar(3), Vigenere(key)]


def test_encrypt():
    method = ProductCipher(ciphers)
    res = method.encrypt(message)
    assert res == ciphertext


def test_decrypt():
    method = ProductCipher(ciphers)
    res = method.decrypt(ciphertext)
    assert res == message
