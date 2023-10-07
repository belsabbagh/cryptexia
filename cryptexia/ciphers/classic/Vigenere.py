from ..__base import CipherBase
from typing import Literal
from ... import char_ops as co
from ...keygen import generate_repeating_key


class Vigenere(CipherBase):
    def __init__(self, key: str, mode: Literal["auto", "repeat"] = "repeat") -> None:
        if mode not in ["auto", "repeat"]:
            raise ValueError("Invalid mode. Mode must be 'auto' or 'repeat'.")
        self.key = key.upper()
        self.mode = mode
        super().__init__()

    def __make_key(self, data: str) -> str:
        data_len = len(data)
        key = self.key
        if self.mode == "auto":
            return (self.key + data)[:data_len]
        if len(key) > data_len:
            return key[:data_len]
        return generate_repeating_key(key, data_len)

    def encrypt(self, data: str) -> str:
        key = self.__make_key(data)
        cipher_text = [co.add_chars(data[i], key[i]) for i in range(len(data))]
        return "".join(cipher_text)

    def decrypt(self, data: str) -> str:
        key = self.__make_key(data)
        plain_text = [co.sub_chars(data[i], key[i]) for i in range(len(data))]
        return "".join(plain_text)
