def late_bound_callbacks() -> list[object]:
    return [lambda: number for number in range(3)]
