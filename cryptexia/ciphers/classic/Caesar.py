from ..__base import CipherBase, dtype


class Caesar(CipherBase):
    def __init__(self, key: int):
        super().__init__()
        try:
            self.key = int(key)
        except ValueError:
            raise ValueError("Invalid key. Key must be an integer.")

    def encrypt(self, data: dtype) -> dtype:
        return "".join(
            chr((ord(c) + self.key - 65) % 26 + 65)
            if c.isupper()
            else chr((ord(c) + self.key - 97) % 26 + 97)
            if c.islower()
            else c
            for c in data
        )

    def decrypt(self, data: dtype) -> dtype:
        return "".join(
            chr((ord(c) - self.key - 65) % 26 + 65)
            if c.isupper()
            else chr((ord(c) - self.key - 97) % 26 + 97)
            if c.islower()
            else c
            for c in data
        )
