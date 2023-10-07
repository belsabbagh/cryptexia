from cryptexia.ciphers.product import ProductCipher
from cryptexia.ciphers.classic import Caesar
from cryptexia.ciphers.classic import Vigenere

message = "abc".upper()
key = "key".upper()
ciphertext = "nid".upper()


def test_encrypt():
    method = ProductCipher([Caesar(3), Vigenere(key)])
    res = method.encrypt(message)
    assert res == ciphertext


def test_decrypt():
    method = ProductCipher([Caesar(3), Vigenere(key)])
    res = method.decrypt(ciphertext)
    assert res == message
