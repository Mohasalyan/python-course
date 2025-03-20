def slice_string(text: str, start: int = 0, end: int = None, step: int = 1) -> str:
    """
    Returns a sliced version of the string.
    """
    return text[start:end:step]


def reverse_string(text: str) -> str:
    """
    Returns the reversed string.
    """
    return text[::-1]
