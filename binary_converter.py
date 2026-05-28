"""Binary converter module"""


def dec_to_bin(n: int) -> str:
    """Converts a number from 0 to 100 to its binary representation."""
    if not isinstance(n, int):
        raise TypeError("The number must be an integer.")
    if n < 0 or n > 100:
        raise ValueError("The number is out of the allowed range.")
    return bin(n)[2:]
