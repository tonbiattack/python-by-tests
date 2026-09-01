from collections.abc import Iterator


def numbers() -> Iterator[int]:
    return iter([1, 2, 3])
