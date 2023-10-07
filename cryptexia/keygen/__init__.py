import random
import string


def generate_random_key(key_len: int):
    return "".join(random.choice(string.ascii_letters) for _ in range(key_len))


def generate_repeating_key(keyword: str, key_len: int):
    return (keyword * (key_len // len(keyword) + 1))[:key_len]
