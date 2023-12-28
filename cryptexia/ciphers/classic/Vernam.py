from ... import keygen as kg
from ..__base import dtype, CipherBase
def xor(char: str, key: str) -> str:
    return chr(ord(char) ^ ord(key))

class Vernam:
    def __init__(self) -> None:
        super().__init__()

    def encrypt(self, data: dtype) -> tuple[dtype, str]:
        key = kg.generate_random_key(len(data))
        return "".join(xor(c, k) for c, k in zip(data, key)), key

    def decrypt(self, data: dtype, key: str) -> dtype:
        return "".join(xor(c, k) for c, k in zip(data, key))

class SimVernam(CipherBase):
    def __init__(self, key) -> None:
        super().__init__()
        self.key: str = key

    def encrypt(self, data: dtype) -> str:
        return "".join(xor(c, k) for c, k in zip(data, self.key))

    def decrypt(self, data: dtype) -> dtype:
        return "".join(xor(c, k) for c, k in zip(data, self.key))
