from abc import abstractmethod
from typing import TypeAlias

dtype: TypeAlias = str


class CipherBase:
    @abstractmethod
    def encrypt(self, data: dtype) -> dtype:
        pass

    @abstractmethod
    def decrypt(self, data: dtype) -> dtype:
        pass
