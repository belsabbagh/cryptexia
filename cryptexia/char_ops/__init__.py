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


def ascii2char(char_code: int) -> str:
    """Converts an ascii char code to a char."""
    return chr(char_code)


def add_chars(char1: str, char2: str, alpha_sequence=None) -> str:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Adds two chars in the alphabet sequence."""
    return int2char(
        (char2int(char1, alpha_sequence) + char2int(char2, alpha_sequence))
        % len(alpha_sequence),
        alpha_sequence,
    )


def sub_chars(char1: str, char2: str, alpha_sequence=None) -> str:
    if alpha_sequence is None:
        alpha_sequence = ascii_uppercase
    """Subtracts two chars in the alphabet sequence."""
    return int2char(
        (char2int(char1, alpha_sequence) - char2int(char2, alpha_sequence))
        % len(alpha_sequence),
        alpha_sequence,
    )
