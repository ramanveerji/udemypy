# Markdown special characters
SPECIAL_CHARS = (
    "_",
    "*",
    "[",
    "]",
    "(",
    ")",
    "~",
    "`",
    ">",
    "#",
    "+",
    "-",
    "=",
    "|",
    "{",
    "}",
    ".",
    "!",
)


def get_valid_text(text):
    """
    Returns the text but with a backslash added behind all special characters
    """
    return "".join(
        f"\\{character}" if character in SPECIAL_CHARS else character
        for character in str(text)
    )
