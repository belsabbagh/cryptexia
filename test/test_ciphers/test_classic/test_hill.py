from cryptexia.ciphers.classic import Hill

message = "meetmeattheusualplaceattenratherthaneightoclock".upper()
expected = "YYBTYYRDYVGACEDZIHKOKQGBXDXQYVRFYVNNYULVHSVHGSXT"


def test_encrypt():
    method = Hill("9,4\n5,7")
    res = method.encrypt(message)
    assert res == expected


def test_decrypt():
    method = Hill("9,4\n5,7")
    res = method.decrypt(expected)
    assert res == message + "X"


def test_key_not_square_error():
    try:
        _ = Hill("9,45,7")
        assert False
    except ValueError as e:
        assert str(e) == "Invalid key. Matrix must be square."


def test_key_not_invertible():
    try:
        _ = Hill("2,4\n1,2")
        assert False
    except ValueError as e:
        assert str(e) == "Invalid key. Matrix is not invertible."
