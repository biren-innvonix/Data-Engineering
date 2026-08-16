def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("numbers cannot be empty")

    return sum(numbers) / len(numbers)


def is_even(number: int) -> bool:
    return number % 2 == 0