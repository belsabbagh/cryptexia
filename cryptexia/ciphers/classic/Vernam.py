from ..__base import CipherBase
from ... import char_ops as co


class Vernam(CipherBase):
    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__()

    def __process_data(self, data: str) -> str:
        fn = lambda c, k: c ^ k
        return "".join(fn(c, k) for c, k in zip(data, self.key))

    def encrypt(self, data: str) -> str:
        return self.__process_data(data)

    def decrypt(self, data: str) -> str:
        return self.__process_data(data)
