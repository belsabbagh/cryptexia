import numpy as np
from ..__base import CipherBase
from ... import char_ops as co


def __get_substrings(text, size):
    substrings = []
    for i in range(0, len(text), size):
        substrings.append(text[i : i + size])
    return substrings


def matmul(block, key):
    return np.matmul(block, key) % 26


def process_data(data: str, matrix):
    subs = __get_substrings(data, len(matrix))
    sub_vectors = [[co.char2int(i) for i in block] for block in subs]
    res_vectors = [matmul(block, matrix) for block in sub_vectors]
    res_chars = ["".join([co.int2char(i) for i in block]) for block in res_vectors]
    return "".join(res_chars)


def mod_inverse(a, m):
    """
    Calculate the modular multiplicative inverse of 'a' modulo 'm'.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Inverse does not exist


def matrix_inverse_mod26(matrix):
    det = int(round(np.linalg.det(matrix)))
    det_inverse = mod_inverse(det, 26)
    if det_inverse is None:
        raise np.linalg.LinAlgError
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(int)
    inverse_mod26 = (adjugate * det_inverse) % 26
    return inverse_mod26


def guard_matrix(matrix):
    if not all([len(row) == len(matrix) for row in matrix]):
        raise ValueError("Invalid key. Matrix must be square.")
    if len(matrix) < 2:
        raise ValueError("Invalid key. Matrix must be at least 2x2.")
    if np.linalg.det(matrix) == 0:
        raise ValueError("Invalid key. Matrix is not invertible.")
    if not all([all([isinstance(num, int) for num in row]) for row in matrix]):
        raise ValueError("Invalid key. Matrix must contain integers.")
    return True


class Hill(CipherBase):
    def __init__(self, key: str) -> None:
        try:
            mat = self.__parse_csv(key)
        except ValueError:
            raise ValueError("Invalid key. Matrix does not follow csv format.")
        guard_matrix(mat)
        self.key = mat
        super().__init__()

    def __parse_csv(self, csv: str) -> list[list[int]]:
        return [[int(num) for num in row.split(",")] for row in csv.split("\n")]

    def encrypt(self, data: str) -> str:
        data = data.upper()
        while len(data) % len(self.key) != 0:
            data += "X"
        return process_data(data, np.array(self.key))

    def decrypt(self, data: str) -> str:
        data = data.upper()
        if len(data) % len(self.key) != 0:
            raise ValueError("Invalid cipher text.")
        try:
            return process_data(data, matrix_inverse_mod26(np.array(self.key)))
        except np.linalg.LinAlgError:
            raise ValueError("Invalid key. Matrix is not invertible.")
