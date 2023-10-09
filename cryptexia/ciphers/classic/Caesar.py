from ..__base import CipherBase, dtype
from ... import char_ops as co


class Caesar(CipherBase):
    def __init__(self, key: int):
        super().__init__()
        try:
            self.key = int(key)
        except ValueError:
            raise ValueError("Invalid key. Key must be an integer.")

    def encrypt(self, data: dtype) -> dtype:
        return "".join(
            co.int2char(co.char2int(c) + self.key)
            for c in data
        )

    def decrypt(self, data: dtype) -> dtype:
        return "".join(
            co.int2char(co.char2int(c) - self.key)
            for c in data
        )
