def reverse_string(value: str) -> str:
    return value[::-1]


def is_palindrome(value: str) -> bool:
    value = value.lower()
    return value == value[::-1]