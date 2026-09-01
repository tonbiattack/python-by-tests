def doubled(values: list[int], calls: list[int]):
    for value in values:
        calls.append(value)
        yield value * 2
