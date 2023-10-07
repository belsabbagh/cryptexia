from ..__base import CipherBase


class ProductCipher(CipherBase):
    def __init__(self, ciphers: list[CipherBase]):
        self.ciphers = ciphers

    def encrypt(self, data: str) -> str:
        ciphertext = data
        for cipher in self.ciphers:
            ciphertext = cipher.encrypt(ciphertext)
        return ciphertext

    def decrypt(self, data: str) -> str:
        plaintext = data
        for cipher in reversed(self.ciphers):
            plaintext = cipher.decrypt(plaintext)
        return plaintext

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.ciphers})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.ciphers})"
