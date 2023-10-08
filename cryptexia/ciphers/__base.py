from abc import abstractmethod


dtype = [str, bytes]


class CipherBase:
    @abstractmethod
    def encrypt(self, data: dtype) -> dtype:
        pass

    @abstractmethod
    def decrypt(self, data: dtype) -> dtype:
        pass
