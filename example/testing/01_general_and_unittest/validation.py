VOWELS = frozenset("aeiouаеєиіїоуюя")


def read_positive_number() -> int:
    raw = input("Введіть додатне ціле число: ")
    try:
        number = int(raw)
    except ValueError:
        raise ValueError("Потрібно ввести ціле число") from None
    if number <= 0:
        raise ValueError("Число має бути додатним")
    return number


def count_vowels(text: str) -> int:
    return sum(letter in VOWELS for letter in text.lower())
