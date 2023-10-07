from string import ascii_uppercase


def ascii2int(char_code: int, alpha_sequence=None) -> int:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Converts an ascii char code to an integer index in the alphabet sequence."""
    return alpha_sequence.index(chr(char_code))


def int2ascii(index: int, alpha_sequence=None) -> str:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Converts an integer index in the alphabet sequence to an ascii char code."""
    return alpha_sequence[index]


def char2int(char: str, alpha_sequence=None) -> int:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Converts a char to an integer index in the alphabet sequence."""
    return alpha_sequence.index(char)


def int2char(index: int, alpha_sequence=None) -> str:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Converts an integer index in the alphabet sequence to a char."""
    return alpha_sequence[index]
