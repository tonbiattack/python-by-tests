def shared_rows() -> list[list[str]]:
    return [[]] * 3


def independent_rows() -> list[list[str]]:
    return [[] for _ in range(3)]
