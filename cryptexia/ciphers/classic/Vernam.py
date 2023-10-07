from ... import keygen as kg


class Vernam:
    def __init__(self) -> None:
        super().__init__()

    def __xor(self, char: str, key: str) -> str:
        return chr(ord(char) ^ ord(key))

    def encrypt(self, data: str) -> tuple[str, str]:
        key = kg.generate_random_key(len(data))
        return "".join(self.__xor(c, k) for c, k in zip(data, key)), key

    def decrypt(self, data: str, key: str) -> str:
        return "".join(self.__xor(c, k) for c, k in zip(data, key))
