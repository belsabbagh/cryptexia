from ..__base import CipherBase


class Vernam(CipherBase):
    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__()

    def __process_data(self, data: str) -> str:
        def __xor(a: str, b: str) -> str:
            return chr((ord(a) % 26 ^ ord(b) % 26) + 65)

        return "".join(__xor(c, k) for c, k in zip(data, self.key))

    def encrypt(self, data: str) -> str:
        return self.__process_data(data)

    def decrypt(self, data: str) -> str:
        return self.__process_data(data)
