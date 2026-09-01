import copy


def shallow(values: list[list[str]]) -> list[list[str]]:
    return values.copy()


def deep(values: list[list[str]]) -> list[list[str]]:
    return copy.deepcopy(values)
