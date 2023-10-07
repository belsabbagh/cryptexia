from cryptexia.ciphers.classic import Vernam


def test_encrypt():
    vernam = Vernam("OCVHW")
    data = "HELLO"
    assert vernam.encrypt(data) == "OFJNRWCB"


def test_decrypt():
    vernam = Vernam("OCVHW")
    data = "JGEMY"
    assert vernam.decrypt(data) == "HELLO"
