from ... import keygen as kg
from ..__base import dtype


class Vernam:
    def __init__(self) -> None:
        super().__init__()

    def __xor(self, char: str, key: str) -> str:
        return chr(ord(char) ^ ord(key))

    def encrypt(self, data: dtype) -> tuple[dtype, str]:
        key = kg.generate_random_key(len(data))
        return "".join(self.__xor(c, k) for c, k in zip(data, key)), key

    def decrypt(self, data: dtype, key: str) -> dtype:
        return "".join(self.__xor(c, k) for c, k in zip(data, key))
